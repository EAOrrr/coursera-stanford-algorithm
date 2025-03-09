
def build_list(filename):
    f = open(filename, "r")
    lines = f.readlines()
    num_of_vertices = int(lines[0])
    weights = [int(w_str) for w_str in lines[1:]]
    return num_of_vertices, weights

def mwis_bottom_up(n, weights):
    dp = [0 for _ in range(n+1)]
    dp[1] = weights[0]
    for i in range(2, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + weights[i-1])
    return dp

def mwis_memorized(n, weights):
    dp = [None for _  in range(n+1)]
    mwis_memorized_helper(n, weights, dp)
    return dp

def mwis_memorized_helper(n, weights, dp):
    if dp[n] is not None:
        return dp[n]
    if n == 0:
        q = 0
    elif n == 1:
        q = weights[0]
    else:
        q = mwis_memorized_helper(n-1, weights, dp)
        q = max(q, mwis_memorized_helper(n-2, weights, dp) + weights[n-1])
    dp[n] = q
    return q

def reconstruct(n, dp, weights):
    choose = [0 for _ in range(n+1)]
    idx = n
    while idx >= 0:
        if dp[idx-1] < dp[idx-2] + weights[idx-1]:
            choose[idx] = 1
            idx -= 2
        else:
            idx -= 1
    return choose

n, weights = build_list("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week03/mwis.txt")
# ans_memorized = mwis_memorized(n, weights)
# print(ans_memorized)
ans_bottom_up = mwis_bottom_up(n, weights)
choices = reconstruct(n, ans_bottom_up, weights)
print("".join([str(choices[i]) for i in [1, 2, 3, 4, 17, 117, 517, 997]]))
