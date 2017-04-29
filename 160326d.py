from heapq import heappush, heappop
inputs = lambda: map(int, raw_input().split())
 
n, m, t = inputs()
A = inputs()
 
g = [[] for i in xrange(n)]
gr = [[] for i in xrange(n)]
 
for i in xrange(m):
    a, b, c = inputs()
    g[a-1].append([b-1, c])
    gr[b-1].append([a-1, c])
 
def dijkstra(g):
    dist = [10**12]*n
    que = []
    dist[0] = 0
    heappush(que, (0, 0))
    # que.append((0,0))
    while len(que):
        ti, u = heappop(que)
        # u, ti = que.pop()
        if dist[u] < ti:
            continue
 
        for v, c in g[u]:
            if ti + c < dist[v]:
                dist[v] = ti + c
                heappush(que, (ti+c, v))
                # que.append((v, ti + c))
        print que
    return dist
 
dist = dijkstra(g)
distr = dijkstra(gr)

ans = 0
for i in xrange(n):
    rest = t - dist[i] - distr[i]
    if rest > 0:
        ans = max(rest*A[i], ans)
print ans