from queue import Queue
from threading import Thread

def run(values, workers=2):
 q=Queue(4); out=[]
 def worker():
  while True:
   x=q.get()
   if x is None:q.task_done();return
   out.append(x*x);q.task_done()
 ts=[Thread(target=worker) for _ in range(workers)]
 [t.start() for t in ts]
 for x in values:q.put(x)
 for _ in ts:q.put(None)
 q.join();[t.join() for t in ts];return sorted(out)
if __name__=='__main__':print(run(range(10)))
