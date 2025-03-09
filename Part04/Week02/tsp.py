import math
import cProfile

class Solution():
    def __init__(self, filename) -> None:
        self.n, self.vertices = self.read_file(filename)
    
    @staticmethod
    def read_file(filename):
        with open(filename) as f:
            lines = f.readlines()
            n = int(lines[0])
            vertices = [(float(line.split()[0]), float(line.split()[1])) for line in lines[1:]]
            return n, vertices
    
    @staticmethod
    def next_set_of_n_elements(x):
        if x == 0:
            return x
        smallest = x & (-x)
        ripple = x + smallest
        new_smallest = ripple & (-ripple)
        ones = ((new_smallest // smallest) >> 1) - 1
        return ripple | ones
    
    def dist(self, i, j):
        x, y  = self.vertices[i], self.vertices[j]
        return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
    
    def tsp(self):
        # source: n - 1
        only_one = 1 << (self.n -1)

        dp = [{} for _ in range(self.n)]
        dp[self.n - 1][only_one] = 0

        for m in range(0, self.n - 1):
            new_dp = [{} for _ in range(self.n)]
            s = only_one | ((1 << (m+1)) - 1)
            while s < (1 << self.n):
                for j in range(0, self.n):
                    # check if j in S:
                    with_j = 1 << j
                    if s & with_j != 0:
                        # dp[j][s] = float('inf')
                        new_dp[j][s] = float('inf')
                        for k in range(0, self.n):
                            # check if k in S
                            with_k = 1 << k
                            if s & with_k != 0 and k != j:
                                # check if S-{j} in dp[k]:
                                if s & (~with_j) in dp[k]:
                                    # dp[j][s] = min(dp[j][s], dp[k][s & (~with_j)] + self.dist(j, k))
                                    new_dp[j][s] = min(new_dp[j][s], dp[k][s & (~with_j)] + self.dist(j, k))
                s = self.next_set_of_n_elements(s)
                dp = new_dp

        result = float('inf')
        all_set = (1 << self.n) - 1
        for j in range(0, self.n - 1):
            result = min(result, dp[j][all_set] + self.dist(self.n-1, j))
        return result
        

# solution = Solution('/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week02/test.txt')
solution = Solution('/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week02/tsp.txt')
cProfile.run('print(int(solution.tsp()))')