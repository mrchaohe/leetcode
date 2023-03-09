# 矩阵路径问题
"""
矩阵的数目
机器人从m*n d 格子左上角出发，每步向下或向左， 计算到达右下角的数目

e.g 3*3格子为6种
"""

"""
分析 
设到达i,j位置的走法数量为f(i, j), 大小为m*n的格子 f(m-1, n-1)为代码解

状态方程
到达(i,j), 只有两个方向(i-1, j)和(i, j-1)能到该位置，即两个路径之和
f(i, j) = f(i, j-1) + f(i-1, j)


初始化
f(0, j) = 1
f(i, 0) = 1

"""

def marix_path(m, n):
    pass
    dp = [[1 for i in range(n)]  for j in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

if __name__ == "__main__":
    print(marix_path(3, 3))

