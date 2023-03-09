# 房屋偷盗 
"""
输入一个数组表示某条街道上房屋内财产的数量， 如果相邻被偷则会报警，计算小偷在街上最大偷盗财产
e.g [2,3,4,5,3]


逻辑 在f(n) 取f(n-2) + n 与f(n-1)的最大值
f(0) = 0
f(1) = cost[0]
"""


# 方案1 递归

def max_earn1(cost):
    n = len(cost)
    return max(helpher1(cost, n-2), helpher1(cost, n-1))

def helpher1(cost, n):
    if n < 0:
        return 0
    if n == 0:
        return cost[0]
    if n == 1:
        return max(cost[0], cost[1])
    
    return max(helpher1(cost, n-2)+cost[n], helpher1(cost, n-1))


# 方案2 缓存递归
def max_earn2(cost):
    if cost is None or len(cost) == 0:
        return 0
    n = len(cost)
    dp = [0 for i in range(n)]
    helpher2(cost, dp, n-1)
    return dp[n-1]    

def helpher2(cost,dp, i):
    if i == 0:
        dp[0] = cost[0]
    if i == 1:
        dp[1] = max(cost[0], cost[1])
    if dp[i] == 0:
        helpher2(cost, dp, i-2)
        helpher2(cost, dp ,i-1)
        dp[i] = max(dp[i-2]+cost[i], dp[i-1])
    



# 方案3 循环
def max_earn3(cost):
    n = len(cost)
    if n ==0:
        return 0
    if n == 1:
        return max(cost[0])
    dp = [cost[0]]
    if n > 1:
        dp.append(max(cost[0], cost[1]))

    for i in range(2, n):
        dp.append(max(dp[i-2]+cost[i], dp[i-1]))

    return dp[n-1]


# 方案4 2变量循环

def max_earn4(cost):
    n = len(cost)
    if n==0:
        return 0
    if n == 1:
        return cost[0]
    dp = [cost[0]]
    if n > 1:
        dp.append(max(cost[0], cost[1]))


    for i in range(2, n):
        dp[i%2]  = max(dp[(i-2)%2] + cost[i], dp[(i-1)%2])
    
    return dp[(n-1)%2]


# 方案5 2个状态方程
"""
f(i) 表示不进入i房间的最大财务
g(i) 表示进入房间的最大财务

状态方程
f(i) = max(f(i-1), g(i-1))
g(i) = f(i-1) + cost[i]

初始值
f(0) = 0
g(0) = cost[0]
""" 

def max_earn5(cost):
    if cost is None or len(cost) == 0:
        return 0
    
    num = len(cost)
    np = [ [0 for i in range(num)] for j in range(2)] 
    
    np[0][0] = 0
    np[1][0] = cost[0]

    for i in range(1, num):
        np[0][i] = max(np[0][i-1], np[1][i-1])
        np[1][i] = np[0][i-1] + cost[i]

    print(np)
    return max(np[0][num-1], np[1][num-1])

if __name__ == "__main__":
    cost = [2,3,4,5,3]
    # print(maxEarn(cost))
    print(max_earn5(cost))