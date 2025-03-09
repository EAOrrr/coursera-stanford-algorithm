from minPQ import MinPQ
from uf import WeightedPCUF, RankPCUF
from collections import deque

class NodeKeyPair():
    def __init__(self, node, key) -> None:
        self.node = node
        self.key = key

    def __lt__(self, other):
        return self.key < other.key or (self.key == other.key and self.node < other.node)

    def __gt__(self, other):
        return self.key > other.key or (self.key == other.key and self.node > other.node)
    
    def __le__(self, other):
        return self.key <= other.key or (self.key == other.key and self.node <= other.node)
    
    def __ge__(self, other):
        return self.key >= other.key or (self.key == other.key and self.node >= other.node)  
    
class Graph():

    def __init__(self, num_of_vertices, num_of_edges):
        self.num_of_vertices = num_of_vertices
        self.num_of_edges = num_of_edges
        self.adj = [[] for _ in range(num_of_vertices)]
        self.edges = []

    def add_edge(self, u, v, c):
        self.adj[u].append((v, c))
        self.edges.append((u, v, c))
    
    def naive_prim(self):
        edge_cost = 0
        visited = {0}
        while len(visited) != self.num_of_vertices:
            min_cost_edge = float('inf')
            v_chosen = None
            for u in visited:
                for v, c in self.adj[u]:
                    if v not in visited and c < min_cost_edge:
                        v_chosen = v
                        min_cost_edge = c
            visited.add(v_chosen)
            edge_cost += min_cost_edge
        return edge_cost

    def heap_prim(self):
        edge_cost = 0
        pq = MinPQ()
        node_key_pairs = [NodeKeyPair(n, float('inf')) for n in range(self.num_of_vertices)]
        node_key_pairs[0] = NodeKeyPair(0, 0)
        for nkp in node_key_pairs:
            pq.insert(nkp)
        while len(pq) != 0:
            min_nkp = pq.extract_min()
            node, cost = min_nkp.node, min_nkp.key
            edge_cost += cost
            for v, c in self.adj[node]:
                node_key_pairs[v].key = min(node_key_pairs[v].key, c)
                pq.decrease_key(node_key_pairs[v])
        return edge_cost
            


    def uf_kruskal(self):
        sorted_edges = sorted(self.edges, key=lambda e: e[2])
        # uf = WeightedPCUF(self.num_of_vertices)
        uf = RankPCUF(self.num_of_vertices)
        edge_cost = 0
        for u, v, c in sorted_edges:
            if uf.find(u) != uf.find(v):
                edge_cost += c
                uf.union(u, v)
        return edge_cost


def build_graph():
    f = open("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week01/edges.txt", "r")
    lines = f.readlines()
    n, m = [int(d) for d in lines[0].split()]
    g = Graph(n, m)
    for line in lines[1:]:
        u, v, c = [int(d) for d in line.split()]
        g.add_edge(u-1, v-1, c)
        g.add_edge(v-1, u-1, c)
    return g

g = build_graph()
print(g.naive_prim())
print(g.heap_prim())
# print(g.naive_kruskal())
print(g.uf_kruskal())
