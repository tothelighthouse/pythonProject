# coding=utf-8
import collections

# 슈도 코드
# BellmanFord(G,w,s):
# //초기화 과정
# for each u in G.V:     //노드를 초기화 하기
#       distance[v] = inf      //모든 노드의 최단거리를 무한으로 지정
#       parent[v] = null       //모든 노드의 부모 노드를 널값으로 지정
# distance[s] = 0 //출발점의 최단거리는 0으로 지정한다
# //거리측정 과정
# for i from 1 to len(G.V):   //노드의 숫자만큼
#      for each (u,v) in G.E:   //모든 변을 체크해 최단 거리를 찾아본다.
#           if distance[u] + w[(u,v)] < distance[v]:
#           //만약 u를 경유하여 v로 가는 거리가 현재 v의 최단 거리보다 짧으면
#                distance[v] = distance[u] + w[(u,v)]  //그 거리를 v의 최단거리로 지정
#                parent[v] = u   //u를 v의 부모 노드로 지정
# //음수 사이클 체크 과정
# for each (u,v) in G.E:
#      if distance[u] + w[(u,v)] < distance[v]:
#           return false //음수 사이클을 확인하고 알고리즘을 정지
# return distance[], parent[]
# 실제 구현
# ...
import inputs as inputs

graph = collections.defaultdict(list)

for u, v, w in inputs:  # 양방향 그래프라고 가정
    graph[u].append([v, w])
    graph[v].append([u, w])

INF = 3000
V = 2000


def bellman_ford(s):
    dist = [INF] * (V + 1)  # V는 노드의 개수
    dist[s] = 0  # 시작 노드의 거리는 0으로 설정
    for _ in range(V - 1):
        for u in range(1, V + 1):
            for v, c in graph[u]:
                if dist[v] > dist[u] + c:
                    dist[v] = dist[u] + c
    for u in range(1, V + 1):  # 음수 사이클이 존재하는지 체크
        for v, c in graph[u]:
            if dist[v] > dist[u] + c:
                return False
    return dist




















