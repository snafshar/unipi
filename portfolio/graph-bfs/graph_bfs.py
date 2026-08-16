from collections import deque

def shortest_path(graph, source, target):
    queue, parent = deque([source]), {source: None}
    while queue:
        node = queue.popleft()
        if node == target: break
        for nxt in graph.get(node, []):
            if nxt not in parent: parent[nxt] = node; queue.append(nxt)
    if target not in parent: return []
    path=[]; node=target
    while node is not None: path.append(node); node=parent[node]
    return path[::-1]

if __name__ == "__main__":
    g={"A":["B","C"],"B":["D"],"C":["D","E"],"D":[],"E":[]}
    print(shortest_path(g,"A","E"))
