import math,random
def sig(x):return 1/(1+math.exp(-x))
if __name__=='__main__':
 random.seed(7); data=[([0,0],0),([0,1],1),([1,0],1),([1,1],0)]
 w=[[random.uniform(-1,1) for _ in range(2)] for _ in range(2)]; v=[random.uniform(-1,1) for _ in range(2)]; b=[0.,0.]; o=0.
 for _ in range(20000):
  for x,t in data:
   h=[sig(sum(w[j][i]*x[i] for i in range(2))+b[j]) for j in range(2)]; y=sig(sum(v[j]*h[j] for j in range(2))+o); out=y-t
   hidden=[out*v[j]*h[j]*(1-h[j]) for j in range(2)]
   for j in range(2):
    v[j]-=.5*out*h[j]; b[j]-=.5*hidden[j]
    for i in range(2): w[j][i]-=.5*hidden[j]*x[i]
   o-=.5*out
 print([round(sig(sum(v[j]*sig(sum(w[j][i]*x[i] for i in range(2))+b[j]) for j in range(2))+o),2) for x,_ in data])
