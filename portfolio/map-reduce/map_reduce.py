from collections import Counter
from concurrent.futures import ThreadPoolExecutor

def map_reduce(words, parts=4):
 chunks=[words[i::parts] for i in range(parts)]
 with ThreadPoolExecutor(parts) as pool: partial=list(pool.map(Counter,chunks))
 total=Counter()
 for item in partial: total.update(item)
 return dict(sorted(total.items()))
if __name__=='__main__':print(map_reduce('parallel systems need careful parallel systems'.split()))
