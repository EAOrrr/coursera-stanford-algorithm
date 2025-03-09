class WeightedPCUF():
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def union(self, u, v):
        u_p = self.find(u)
        v_p = self.find(v)
        if u_p == v_p:
            return
        if self.size[u_p] < self.size[v_p]:
            self.parent[u_p] = v_p
            self.size[v_p] += self.size[u_p]
        else:
            self.parent[v_p] = u_p
            self.size[u_p] += self.size[v_p]
    
    def find(self, x):
        while x != self.parent[x]: 
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

class RankPCUF():
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def union(self, u, v):
        u_p = self.find(u)
        v_p = self.find(v)
        if u_p == v_p:
            return
        if self.rank[u_p] < self.rank[v_p]:
            self.parent[u_p] = v_p
        elif self.rank[u_p] > self.rank[v_p]:
            self.parent[v_p] = u_p
        else:
            self.parent[u_p] = v_p
            self.rank[v_p] += 1
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x