import pstats
import cProfile

def build_list(filename):
    f = open(filename)
    lines = f.readlines()
    knapsack_size, number_of_items = [int(i) for i in lines[0].split()]
    value_weight_pairs = []
    for line in lines[1:]:
        v, w = [int(i) for i in line.split()]
        value_weight_pairs.append((v, w))
    return knapsack_size, number_of_items, value_weight_pairs

def knapsack(size, total_items, items):
    dp = [[0 for _ in range(size + 1)] for _ in range(total_items + 1)]
    for i, (v, w) in enumerate(items):
        for j in range(1, size + 1):
            dp[i+1][j] = dp[i][j]
            if j - w >= 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-w] + v)
    return dp[total_items][size]



def knapsack2(size, items, total):
    dp = [{0:0} for _ in range(total+1)]
    size_to_compute = {size}
    for i in range(total, 0, -1):
        for sz in size_to_compute.copy():
            dp[i][sz] = None if sz > 0 else 0
            _, w = items[i-1]
            if sz - w  > 0:
                size_to_compute.add(sz-w)
    for sz in dp[1]:
        v, w = items[0]
        dp[1][sz] = 0 if sz < w else v

    for i in range(2, total+1):
        v, w = items[i-1]
        for sz in dp[i]:
            dp[i][sz] = dp[i-1][sz]
            if sz - w >= 0:
                dp[i][sz] = max(dp[i][sz], dp[i-1][sz-w] + v)
    return dp[total][size]
                



size1, numbers1, items1 = build_list("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week04/knapsack1.txt")
# size2, numbers2, items2 = build_list("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week04/knapsack_big.txt")
# size0, numbers0, items0 = build_list("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week04/test.txt")
# print(size, numbers, items)
# print(knapsack(size1, numbers1, items1))
# print(knapsack(size0, numbers0, items0))
# print(knapsack2(size0, items0, numbers0))
# print(knapsack2(size1, items1, numbers1))
# print(knapsack2(size2, items2, numbers2))

# "print(clustering_big('/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week02/clustering_big.txt'))"
# cProfile.run("print(knapsack2(size2, items2, numbers2))")
cProfile.run("print(knapsack(size1, numbers1, items1))")
cProfile.run("print(knapsack2(size1, items1, numbers1))")
# p = pstats.Stats("my_func_stats")
# p.sort_stats("cumulative").print_stats()