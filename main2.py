import collections
import inputs as inputs
graph = collections.defaultdict(list)


for u, v, w in inputs:
   graph[u].append([v, w])
   graph[v].append([u, w])




INF = 3434
V = 2000

def bf(s):
    dist = [INF] * (V + 1)
    dist[s] = 0
    for _ in range(V - 1):
        for u in range(1, V + 1):
            if dist[V] > dist[u] + c:
                dist[v] = dist[u] + c
    for u in range(1, v + 1)
        for v, c in graph[u]:












