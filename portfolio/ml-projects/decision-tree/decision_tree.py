def gini(labels):
 n=len(labels); return 1-sum((labels.count(v)/n)**2 for v in set(labels))
def best_split(x,y):
 best=(1,None,None)
 for f in range(len(x[0])):
  for t in sorted(set(r[f] for r in x)):
   left=[y[i] for i,r in enumerate(x) if r[f]<=t]; right=[y[i] for i,r in enumerate(x) if r[f]>t]
   if not left or not right:continue
   score=(len(left)*gini(left)+len(right)*gini(right))/len(y)
   if score<best[0]:best=(score,f,t)
 return best
if __name__=='__main__':print(best_split([[0],[1],[4],[5]],['A','A','B','B']))
