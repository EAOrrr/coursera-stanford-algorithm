from collections import deque
import heapq
class Node():
    def __init__(self, k = None, l = None, r = None) -> None:
        self.key = k
        self.left = l
        self.right = r
    
    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key
    

def huffman_naive():
    pass

def huffman_heap(weights):
    pq = [Node(k=w) for w in weights]
    heapq.heapify(pq)
    while len(pq) > 1:
        n1 = heapq.heappop(pq)
        n2 = heapq.heappop(pq)
        new_node = Node(k=n1.key+n2.key, l=n1, r=n2)
        heapq.heappush(pq, new_node)
    return heapq.heappop(pq)
    

def huffman_two_queue(weights):
    q1 = deque(sorted([Node(k=w) for w in weights]))
    q2 = deque()
    while len(q1) + len(q2) > 1:
        min1 = min_pop(q1, q2)
        min2 = min_pop(q1, q2)
        q2.append(Node(k=min1.key+min2.key, l=min1, r=min2))
    return q2.popleft()

def min_pop(q1, q2):
    if len(q1) == 0:
        return q2.popleft()
    elif len(q2) == 0:
        return q1.popleft()
    if q1[0] < q2[0]:
        return q1.popleft()
    else:
        return q2.popleft()

def build_list(filename):
    f = open(filename, "r")
    lines = f.readlines()
    numbers_of_symbols = int(lines[0])
    weights = [int(w_str) for w_str in lines[1:]]
    return numbers_of_symbols, weights

def max_length(x: Node) -> int:
    if x is None:
        return -1
    return max(max_length(x.left),  max_length(x.right)) + 1

def min_length(x: Node) -> int:
    if x is None:
        return -1
    return min(min_length(x.left), min_length(x.right)) + 1

number_of_symbols, weights = build_list("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week03/huffman.txt")
# number_of_symbols, weights = build_list("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week03/test.txt")
root_heap = huffman_heap(weights)
root_queue= huffman_two_queue(weights)
print(max_length(root_heap), min_length(root_heap))
print(max_length(root_queue), min_length(root_queue))