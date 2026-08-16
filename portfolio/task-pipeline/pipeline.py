#!/usr/bin/env python3
"""A bounded producer/worker/consumer pipeline."""
from __future__ import annotations
import argparse
import queue
import threading
from dataclasses import dataclass

@dataclass(frozen=True)
class Result:
    index: int
    value: int

def run(items: list[int], workers: int = 2, queue_size: int = 8) -> list[int]:
    if workers < 1 or queue_size < 1:
        raise ValueError("workers and queue_size must be positive")
    tasks: queue.Queue[tuple[int, int] | None] = queue.Queue(maxsize=queue_size)
    results: queue.Queue[Result | BaseException] = queue.Queue()
    def worker() -> None:
        while True:
            task = tasks.get()
            try:
                if task is None:
                    return
                index, value = task
                results.put(Result(index, value * value))
            except BaseException as exc:
                results.put(exc)
            finally:
                tasks.task_done()
    pool = [threading.Thread(target=worker, daemon=True) for _ in range(workers)]
    for thread in pool: thread.start()
    for index, value in enumerate(items): tasks.put((index, value))
    for _ in pool: tasks.put(None)
    tasks.join()
    ordered: list[Result] = []
    for _ in items:
        result = results.get()
        if isinstance(result, BaseException): raise result
        ordered.append(result)
    for thread in pool: thread.join()
    return [result.value for result in sorted(ordered, key=lambda result: result.index)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--items", type=int, default=20)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--queue-size", type=int, default=8)
    args = parser.parse_args()
    print(run(list(range(args.items)), args.workers, args.queue_size))
