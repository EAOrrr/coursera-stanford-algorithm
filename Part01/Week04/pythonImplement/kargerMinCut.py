import random


class Vertex:
    def __init__(self, es=[]) -> None:
        self.edges = es  # list of incident edges

class Edge:
    def __init__(self, first:Vertex, end:Vertex):
        self.first = first  # the index of first vertex
        self.end = end      # the index of end vertex

class Graph:
    def __init__(self) -> None:
        pass

def readfile():
    file = open("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part01/Week04/kargerMinCut.txt", "r")
    vertices = [Vertex() for _ in range(201)]
    edges = []
    for u in range(1, 201):
        neighbor = [int(v) for v in file.readline().split("\t")[:-1]]  # [:-1] to remove \n
        for v in neighbor:  # u: the index of first, v: the index of end
            if u != v:  # remove self-loop
                edge = Edge(vertices[u], vertices[v])
                edges.append(edge)
                vertices[u].edges.append(edge)
                vertices[v].edges.append(edge)
        for e in vertices[u].edges:
            assert(e.first == vertices[u] or e.end == vertices[u])
    return vertices, edges

def merge(edge:Edge, vertices):
    first_v = edge.first
    end_v = edge.end
    print(type(first_v.edges+end_v.edges))
    new_v = Vertex(first_v.edges+end_v.edges)
    edges = []
    for e in new_v.edges:
        print(e.first is first_v,  e.first is end_v, e.end is e.first, e.end is end_v)
        if e.first != first_v and e.first != end_v and e.end != e.first and e.end != end_v:
            raise RuntimeError("Wront!")
        if e.first is first_v or e.first is end_v:
            e.first = new_v
        if e.end is first_v or e.end is end_v:
            e.end = new_v
        if e.first is not e.end:
            edges.append(e)
    new_v.edges = e
    vertices.remove(first_v)
    vertices.remove(end_v)
    vertices.append(new_v)



def kargerMin(edges, vertices):
    for _ in range(198):
        rm_idx = random.randint(0, len(edges)-1)
        rm_edge = edges.pop(rm_idx)
        merge(rm_edge, vertices)

    return len(edges)

if __name__ == "__main__":
    vertices, edges = readfile()
    n = kargerMin(edges, vertices)
    print(n)
