from uf import WeightedPCUF, RankPCUF
class Graph():
    def __init__(self, n) -> None:
        self.adj = [[] for _ in range(n)]
        self.edges = []
        self.num_of_vertices = n
    
    def add_edge(self, u, v, c):
        self.adj[u].append((v, c))
        self.edges.append((u, v, c))
    
    def cluster(self, k):
        sorted_edges = sorted(self.edges, key=lambda e: e[2])
        connected_compents = self.num_of_vertices
        uf = WeightedPCUF(self.num_of_vertices)
        for u, v, c in sorted_edges:
            if uf.find(u) != uf.find(v):
                if connected_compents <= k:
                    return c
                uf.union(u, v)
                connected_compents -= 1     
        
def build_graph(filename):
    f = open(filename)
    lines = f.readlines()
    number_of_nodes = int(lines[0])
    g = Graph(number_of_nodes)
    for line in lines[1:]:
        u, v, c = [int(i) for i in line.split()]
        g.add_edge(u-1, v-1, c)
        g.add_edge(v-1, u-1, c)
    return g



# g = build_graph("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week02/input_completeRandom_30_1024.txt")
g = build_graph("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week02/clustering1.txt")
print(g.cluster(4))
