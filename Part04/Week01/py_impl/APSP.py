from minPQ import MinPQ
import cProfile

class NodeKeyPair():
    def __init__(self, node, dist):
        self.node = node
        self.dist = dist

    def __lt__(self, p):
        return self.dist < p.dist 
    
    def __gt__(self, p):
        return self.dist > p.dist 

    def __le__(self, p):
        return self.dist <= p.dist

    def __ge__(self, p):
        return self.dist >= p.dist

class Graph():
    def __init__(self, n) -> None:
       self.size = n
       self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))

    def floyd_warshall_asyn(self):
        dp = [[float('inf') for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            dp[i][i] = 0
        for i in range(self.size):
            for j, w in self.adj[i]:
                dp[i][j] = w
        # recurse
        for k in range(1, self.size):
            for i in range(self.size):
                for j in range(self.size):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        # check negative cycle
        for i in range(self.size):
            if dp[i][i] < 0:
                return False, None
        return True, dp
    
    def floyd_warshall_space_opt(self):
        # dp(i, j, k) = min(dp(i, j, k-1), dp(i, k, k-1) + dp(k, j, k-1))
        dp_prev = [[float('inf') for _ in range(self.size)] for _ in range(self.size)] 
        dp_curr = [[None for _ in range(self.size)] for _ in range(self.size)]
        # initialize: dp[i, i, 0] = 0, dp[i, j, 0] = w(i, j) or +inf
        for i in range(self.size):
            dp_prev[i][i] = 0
        for i in range(self.size):
            for j, w in self.adj[i]:
                dp_prev[i][j] = w
        # recurse
        for k in range(1, self.size):
            for i in range(self.size):
                for j in range(self.size):
                    dp_curr[i][j] = min(dp_prev[i][j], dp_prev[i][k] + dp_prev[k][j])
            dp_prev = dp_curr
        # check negative cycle
        for i in range(self.size):
            if dp_curr[i][i] < 0:
                return False, None
        return True, dp_curr


    def floyd_warshall_naive(self):
        # dp(i, j, k) = min(dp(i, j, k-1), dp(i, k, k-1) + dp(k, j, k-1))
        dp = [[[float('inf') for _ in range(self.size)] for _ in range(self.size)] for _ in range(self.size)]
        # initialize: dp[i, i, 0] = 0, dp[i, j, 0] = w(i, j) or +inf
        for i in range(self.size):
            dp[0][i][i] = 0
        for i in range(self.size):
            for j, w in self.adj[i]:
                dp[0][i][j] = w
        # recurse
        for k in range(1, self.size):
            for i in range(self.size):
                for j in range(self.size):
                    dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])
        # check negative cycle
        for i in range(self.size):
            if dp[self.size - 1][i][i] < 0:
                print(i, dp[self.size - 1][i][i])
                return False, None
        return True, dp[self.size - 1]
    
    def johnson(self):
        adj = self.adj + [[(i, 0) for i in range(self.size)]]
        # print(adj)
        b, vertex_bias = self.bellman_ford(self.size, adj)
        if not b:
            return b, None
        bias_adj = [[(v, w + vertex_bias[u] - vertex_bias[v]) for v, w in self.adj[u]] for u in range(self.size)]
        dist = []
        # print(bias_adj)
        for u in range(self.size):
            dist.append([l + vertex_bias[v] - vertex_bias[u] for v, l in enumerate(self.dijkstra(u, bias_adj))])
        return True, dist
            
    def bellman_ford(self, src, adj):
        dist = [float('inf') for _ in range(len(adj))]
        dist[src] = 0
        for _ in range(len(adj) - 1):
            for u, u_adj in enumerate(adj):
                for v , w in u_adj:
                    dist[v] = min(dist[v], dist[u] + w)
        for u , u_adj in enumerate(self.adj):
            for v, w in u_adj:
                if dist[v] > dist[u] + w:
                    return False, None
        return True, dist
    
    def dijkstra(self, src, adj):
        nodes = [NodeKeyPair(n, float('inf')) for n in range(len(adj))]
        nodes[src] = NodeKeyPair(src, 0)
        dist = [None for _ in range(len(adj))]
        pq = MinPQ()
        for n in nodes:
            pq.insert(n)
        while len(pq) != 0:
            top = pq.extract_min()
            u, u_dist = top.node, top.dist
            dist[u] = u_dist
            for v, w in adj[u]:
                nodes[v].dist = min(nodes[v].dist, u_dist + w)
                pq.decrease_key(nodes[v])
        # print(dist)
        return dist


def build_graph(filename):
    f = open(filename)
    lines = f.readlines()
    n, _ = [int(i) for i in lines[0].split()]
    g = Graph(n)
    for line in lines[1:]:
        u, v, w = [int(i) for i in line.split()]
        g.add_edge(u - 1, v - 1, w)
        # g.add_edge(v - 1, u - 1, w)
    return g

g1 = build_graph("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week01/g1.txt")
g2 = build_graph("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week01/g2.txt")
g3 = build_graph("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week01/g3.txt")

# cProfile.run("g1.johnson()") # 14.336
# cProfile.run("g2.johnson()") # 14.473
# cProfile.run("g3.johnson()") # 136.208
cProfile.run("g1.floyd_warshall_asyn()") # 444.620
cProfile.run("g2.floyd_warshall_asyn()") # 461.089
cProfile.run("g3.floyd_warshall_asyn()") # 451.528