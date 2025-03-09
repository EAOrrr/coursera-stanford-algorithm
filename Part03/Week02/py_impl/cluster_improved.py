# from networkx.utils import UnionFind
from  uf import RankPCUF
import pstats
import cProfile


def small_distance(n, bits):
    return [n^b for b in bits]

def generate_two_bits_list(b):
    one_bit = [1 << i for i in range(b)]
    two_bits = [1 << i | 1 << j for i in range(b) for j in range(b)]
    bits = one_bit + two_bits + [0]
    return set(bits)

def to_int(line):
    result = 0
    for i in line.split():
        result = result + result + int(i)
    return result

def clustering_big2(filename):
    f = open(filename)
    lines = f.readlines()
    n, b = [int(i) for i in lines[0].split()]
    nodes = [to_int(line) for line in lines[1:]]
    hash_nodes = {}
    for i, node in enumerate(nodes):
        if node in hash_nodes:
            hash_nodes[node].add(i)
        else:
            hash_nodes[node] = {i}
        
    bits = generate_two_bits_list(b)
    uf = RankPCUF(n)
    k = n


    for u, number in enumerate(nodes):
        neighbors = small_distance(number, bits)
        for neighbor in neighbors:
            if neighbor in hash_nodes:
                for v in hash_nodes[neighbor]:
                    if uf.find(u) != uf.find(v):
                        uf.union(u, v)
                        k -= 1
    return k



def clustering_big(filename):
    f = open(filename)
    lines = f.readlines()
    n, b = [int(i) for i in lines[0].split()]
    bits = generate_two_bits_list(b)
    uf = RankPCUF(n)
    # u_find = UnionFind()
    hash_nodes = {}
    k = n

    for u, line in enumerate(lines[1:]):
        number = to_int(line)
        
        for neighbor in small_distance(number, bits):
            if neighbor in hash_nodes:
                for v in hash_nodes[neighbor]:
                    if uf.find(u) != uf.find(v):
                        uf.union(u, v)
                        k -= 1

        if number in hash_nodes:
            hash_nodes[number].add(u)
        else:
            hash_nodes[number] = {u}
    return k

# print(generate_two_bits_list(6), len(generate_two_bits_list(6)))
# print(clustering_big2("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week02/test2.txt"))
# print(clustering_big("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week02/clustering_big.txt"))

cProfile.run("print(clustering_big2('/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week02/clustering_big.txt'))"
, "my_func_stats")
# "print(clustering_big('/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week02/clustering_big.txt'))"

p = pstats.Stats("my_func_stats")
p.sort_stats("cumulative").print_stats()