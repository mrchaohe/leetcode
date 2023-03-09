# 三角形路径之和
"""
在一个由数字组成的三角形中， 第一行有1个数字， 第二行有两个数字，n行有n个数字。
每步只能前往下一行中相邻的数字，计算从顶到底最小数字之和。
e.g
     2
    3 4
   6 5 7
  4 1 8 3
最小路径11(2,3,5,1)

"""

"""
分析
f(i, j) 表示第到达(i,j)最小数字之和, 对n行数字,则min(f(n-1, j)) 为题目的解


状态方程
到达(i,j)位置，必然由(i-1, j-1) 和(i-1, j)到达，则两个取最小值为f(i,j)的路径

              f(i-1, 0) + cost[i][0]    j = 0
 f(i, j) =    min(f(i-1, j-1), f(i-1, j)) + cost[i][j]   j !=0 and j!=i
              f(i-1, j-1) + cost[i][j]  j = i

初始化

f(0, 0) = cost[0][0]
"""

def tri_path(cost):
    m = len(cost)

    dp = [[0] for i in range(m)]
    dp[0][0] = cost[0][0]

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + cost[i][0]
        for j in range(1, i+1):
            if j == i:  #最后一个值
                dp[i].append(dp[i-1][j-1] + cost[i][j])
            else:
                min_syb = min(dp[i-1][j-1], dp[i-1][j])
                dp[i].append(min_syb+cost[i][j])
    return min(dp[m-1])
if __name__ == "__main__":
    cost = [
           [2],
           [3, 1],
           [6, 5, 7],
           [4, 1, 8, 3]
    ]
    print(tri_path(cost))