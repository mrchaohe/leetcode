"""
环形房子
输入一个数组表示某条街道上房屋内财产的数量， 如果相邻被偷则会报警，计算小偷在街上最大偷盗财产， 数组收尾组成一个环
e.g [2,3,4,5,3]


状态方程


0到n-2 和1到n-1能选择的最大数量
         f(n-2)   0~n-2
f(i) = 
         f(n-1)   1~n-1
"""

# 递归
def max_earn(cost):
    if cost is None or len(cost) == 0:
        return 0
    n = len(cost)
    if n == 1:
        return cost[0]
    

    

    return max(helpher(cost, start=0, end=n-2), helpher(cost,start=1,end=n-1))

def helpher(cost, start, end):
    
    #初始化
    dp = [0, 0] 
    dp[0] = cost[start]
    if start < end:
        dp[1] = max(cost[start], cost[start+1])

    
    for i in range(start+2, end+1):
        j = i-start
        dp[j%2] = max(dp[(j-1)%2], dp[(j-2)%2]+cost[i])
    return dp[(end-start)%2]

if __name__ == "__main__":
    syb = [2,3,4,5,3]
    print(max_earn(syb))