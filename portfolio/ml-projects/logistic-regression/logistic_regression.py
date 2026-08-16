import math

def sigmoid(x): return 1/(1+math.exp(-max(-40,min(40,x))))
def fit(x,y,rate=.4,epochs=500):
 w=[0.0]*len(x[0]); b=0.0
 for _ in range(epochs):
  for row,target in zip(x,y):
   error=sigmoid(sum(a*c for a,c in zip(w,row))+b)-target
   w=[a-rate*error*c for a,c in zip(w,row)]; b-=rate*error
 return w,b
if __name__=='__main__':
 x=[[0,0],[0,1],[1,0],[1,1]]; y=[0,0,0,1]; w,b=fit(x,y)
 print([int(sigmoid(sum(a*c for a,c in zip(w,r))+b)>=.5) for r in x])
