def rank(edges, damping=.85, tolerance=1e-10):
    nodes=sorted(set(edges)|{v for vs in edges.values() for v in vs}); n=len(nodes); r={v:1/n for v in nodes}
    for _ in range(1000):
        new={v:(1-damping)/n for v in nodes}; dangling=sum(r[v] for v in nodes if not edges.get(v))
        for u,score in r.items():
            for v in edges.get(u,[]): new[v]+=damping*score/len(edges[u])
        for v in nodes: new[v]+=damping*dangling/n
        if max(abs(new[v]-r[v]) for v in nodes)<tolerance:return new
        r=new
    return r
if __name__=="__main__": print(rank({'a':['b'],'b':['a','c'],'c':[]}))
