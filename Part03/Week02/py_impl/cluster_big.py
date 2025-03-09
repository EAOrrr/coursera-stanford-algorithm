from uf import WeightedPCUF, RankPCUF

def hamming_distance(u, v):
    return sum([i^j for i, j in zip(u, v)])

def clustering_big(filename):
    f = open(filename)
    lines = f.readlines()
    n, b = [int(i) for i in lines[0].split()]
    k = n
    uf = RankPCUF(n)
    nodes = []
    for line in lines[1:]:
        u = [int(i) for i in line.split()]
        for j , v in enumerate(nodes):
            if hamming_distance(u, v) < 3 and uf.find(len(nodes)) != uf.find(j):
                uf.union(len(nodes), j) 
                k -= 1
        nodes.append(u)
    return k

# print(clustering_big("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week02/clustering_big.txt"))
print(clustering_big("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week02/test2.txt"))
# g.cluster()