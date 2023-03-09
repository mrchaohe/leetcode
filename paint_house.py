# 粉刷房子 n*3的数组表示n幢房子分别用三种涂料粉刷的成本,颜色顺序红绿蓝
# e.g [[17,2,16], [15,14,5], [13,3,1]]， 最小成本2,5,3； 10

"""
1. 定义变量
r(i) 表示i幢房子刷成红色的最小成本
g(i) 表示i幢房子刷成绿色的最小成本
b(i) 表示i幢房子刷成蓝色的最小成本

2. 状态方程
r(i) = min(g(i-1), b(i-1)) + nums[i][0]
g(i) = min(r(i-1), b(i-1)) + nums[i][1]
b(i) = min(g(i-1), r(i-1)) + nums[i][2]


# 初始值
r[0] = nums[0][0]
g[0] = nums[0][1]
b[0] = num[0][2]
"""

def paint_house(nums):
    if nums is None or len(nums) == 0:
        return 0
    
    n = len(nums)
    # 初始化赋值
    # dp = [[0 for i in range(n)] for j in range(3)]
    # for j in range(3):
    #     dp[j][0] = nums[0][j]

    dp = [[0,0] for i in range(3)]
    for j in range(3):
        dp[j][0] = nums[0][j]

    for i in range(1, n):
        for j in range(3):
            pre1 = dp[(j+2)%3][(i-1)%2]+nums[i][j]
            pre2 = dp[(j+1)%3][(i-1)%2] + nums[i][j] 
            dp[j][i%2] = min(pre1, pre2)

    return min(dp[0][(n-1)%2], dp[1][(n-1)%2], dp[2][(n-1)%2])

if __name__ == "__main__":
    eg = [[17,2,16], [15,14,5], [13,3,1], [5,4,2]]
    print(paint_house(eg))


# dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + nums[i][0]
        # dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + nums[i][1]
        # dp[2][i] = min(dp[1][i-1], dp[0][i-1]) + nums[i][2]