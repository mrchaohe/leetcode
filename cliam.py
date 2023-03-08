# 爬楼梯,一个数组cost所有数字均为正数，第i个数字表示第i级往上爬的成本，
# 在支付cost[i]后可以向上爬一阶或二阶，求总成本最小
# e.g 输入数组[1,100,1,100,1]
"""
逻辑： 到f(n)共有两条路径， f(n-1) + (n-1)和 f(n-2) + (n-1), 递归取最小值
"""

# 方案1 递归

def helper(cost, n):
    if n < 2:
        return cost[n]
    return min(helper(cost, n-1), helper(cost, n-2)) + cost[n]

def min_cost_clib1(cost):
    if cost is None or len(cost) == 0:
        return 0

    n = len(cost)
    return min(helper(cost, n-1), helper(cost, n-2))

# 方案2 递归缓存

def min_cost_clib2(cost):
    if cost is None or len(cost) == 0:
        return 0
    
    n = len(cost)
    dp = [0 for i in range(n)]
    helpher(cost, dp, n-1)
    return min(dp[n-1], dp[n-2])
    

def helpher(cost, dp, i):
    if i<2:
        dp[i] = cost[i]
    elif dp[i]==0:
        helpher(cost, dp, i-2)
        helpher(cost, dp, i-1)
        dp[i] = min(dp[i-1], dp[i-2])+ cost[i]




# 方案3 循环缓存
def min_cost_clib3(cost):
    if cost is None or len(cost) == 0:
        return 0 
    n = len(cost)
    if n == 1:
        return cost[0]
            
    store = [cost[0], cost[1]]
  
    for i in range(2, len(cost)):
        store.append(min(store[i-1], store[i-2]) + cost[i])
    return min(store[-1], store[-2])


# 缓存o(1)
def min_cost_clib4(cost):
    if cost is None or len(cost) == 0:
        return 0

    dp = [cost[0], cost[1]]
    for i in range(2, len(cost)):
       
        dp[i%2] = min(dp[0], dp[1]) + cost[i]
    
    return min(dp[0], dp[1])


if __name__== "__main__":
    syb = [1, 100, 1, 1, 100, 1, 100]
    # syb = [1, 100, 1]
    # print(min_cost_clib(syb))
    # print(min_cost_clib1(syb))
    print(min_cost_clib2(syb))