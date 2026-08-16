#include <algorithm>
#include <chrono>
#include <cctype>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <thread>
#include <unordered_map>
#include <vector>

using Counts = std::unordered_map<std::string, std::size_t>;

static void count_line(const std::string& line, Counts& counts) {
    std::string word;
    for (unsigned char ch : line) {
        if (std::isalnum(ch)) word.push_back(static_cast<char>(std::tolower(ch)));
        else if (!word.empty()) { ++counts[word]; word.clear(); }
    }
    if (!word.empty()) ++counts[word];
}

static Counts sequential(const std::vector<std::string>& lines) {
    Counts result;
    for (const auto& line : lines) count_line(line, result);
    return result;
}

static Counts parallel(const std::vector<std::string>& lines, unsigned workers) {
    workers = std::max(1u, std::min<unsigned>(workers, lines.empty() ? 1 : lines.size()));
    std::vector<Counts> local(workers);
    std::vector<std::thread> pool;
    for (unsigned id = 0; id < workers; ++id) {
        const std::size_t begin = lines.size() * id / workers;
        const std::size_t end = lines.size() * (id + 1) / workers;
        pool.emplace_back([&, id, begin, end] {
            for (std::size_t i = begin; i < end; ++i) count_line(lines[i], local[id]);
        });
    }
    for (auto& thread : pool) thread.join();
    Counts result;
    for (const auto& counts : local)
        for (const auto& [word, count] : counts) result[word] += count;
    return result;
}

static double timed(const std::vector<std::string>& lines, unsigned workers, Counts& out) {
    const auto start = std::chrono::steady_clock::now();
    out = workers == 1 ? sequential(lines) : parallel(lines, workers);
    return std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();
}

int main(int argc, char** argv) {
    if (argc < 2) { std::cerr << "usage: wordcount FILE [--threads N]\n"; return 2; }
    unsigned workers = 1;
    if (argc == 4 && std::string(argv[2]) == "--threads") workers = std::stoul(argv[3]);
    std::ifstream input(argv[1]);
    if (!input) { std::cerr << "cannot open input file\n"; return 1; }
    std::vector<std::string> lines;
    for (std::string line; std::getline(input, line);) lines.push_back(std::move(line));
    Counts baseline, result;
    const double sequential_time = timed(lines, 1, baseline);
    const double selected_time = timed(lines, workers, result);
    if (baseline != result) throw std::runtime_error("parallel result differs from baseline");
    std::size_t total = 0;
    for (const auto& [_, count] : result) total += count;
    std::cout << "words=" << total << " distinct=" << result.size()
              << " threads=" << workers << " seconds=" << selected_time
              << " speedup=" << sequential_time / selected_time << '\n';
}
