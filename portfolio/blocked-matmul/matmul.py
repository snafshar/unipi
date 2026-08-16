import argparse

def multiply(a,b,tile):
    n=len(a); c=[[0]*n for _ in range(n)]
    for ii in range(0,n,tile):
      for kk in range(0,n,tile):
       for jj in range(0,n,tile):
        for i in range(ii,min(ii+tile,n)):
         for k in range(kk,min(kk+tile,n)):
          for j in range(jj,min(jj+tile,n)): c[i][j]+=a[i][k]*b[k][j]
    return c
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument('--size',type=int,default=8); p.add_argument('--tile',type=int,default=4); x=p.parse_args()
 a=[[i+j for j in range(x.size)] for i in range(x.size)]; print(multiply(a,a,x.tile)[0])
