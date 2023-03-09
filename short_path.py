# 最短路径问题
"""

机器人从m*n d 格子左上角出发，每步向下或向左， 每个格子有数字， 计算到达右下角路径数字之和的最小值

1 3 1
2 5 2
3 4 1

最小路径之和为8( 1 3 1 2 1) 
"""

"""
分析
记f(i, j) 为到达(i,j)位置最小路径， 对m*n, 则f(m-1, n-1)为解


状态方程
到达(i,j), 只有两个方向(i-1, j)和(i, j-1)能到该位置，到达(i, j)即两个路径最小值
f(i, j) = min(f(i, j-1) + f(i-1, j)) + cost[i, j]


初始值
f(0, j) = sum(cost[0, j])
f(i, 0) = sum(cost[i, 0])

"""

def short_path(cost):
    m = len(cost)
    if m == 0:
        return 0
    n = len(cost[0])
    dp = [[0 for i in range(n)] for j in range(m) ]

    # 初始化
    dp[0][0] = cost[0][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + cost[0][j]
    
    
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + cost[i][0]
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + cost[i][j]

    return dp[m-1][n-1]


if __name__ == "__main__":
    cost = [
        [1, 3, 1],
        [2, 5, 2],
        [3, 4, 1]
    ]

    print(short_path(cost))