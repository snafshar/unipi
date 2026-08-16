def kmeans(points,k=2,steps=20):
 c=[list(p) for p in points[:k]]
 for _ in range(steps):
  groups=[[] for _ in range(k)]
  for p in points: groups[min(range(k),key=lambda i:sum((p[j]-c[i][j])**2 for j in range(2)))].append(p)
  new=[([sum(p[0] for p in g)/len(g),sum(p[1] for p in g)/len(g)] if g else c[i]) for i,g in enumerate(groups)]
  if new==c:return c,groups
  c=new
 return c,groups
if __name__=='__main__': print(kmeans([[1,1],[1,2],[8,8],[9,8]]))
