# 双序列问题 最长公共子序列长度
# 输入两个字符串， 求出最长公共字符子序列的长度； 从字符s1 删除若干个字符得到s2， s2就是s1子序列
# e.g abcde  ace ， 但aec不是
# 输入 abcde 和badfe ， 最长子序列bde 3


"""
定义
f(i,j) 表示两个数组最大长度


状态方程
           f(i-1, j-1)+1  s1[i]=s2[j]
f(i, j ) = 
           max(f(i-1,j), f(i, j-1))  s1[i]!= s2[j]


初始化

f(-1, j) = 0
f(i, -1) = 0
f(-1, -1) = 0 
"""

def two_subserquence(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    
    if n1==0 or n2 == 0:
        return 0

    # 初始化第一行, 第一列为0
    dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
    
    for i in range(n1):
        for j in range(n2):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] +1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
    return dp[n1][n2]

if __name__ == "__main__":
    s1 = "abcde"
    s2 = "badfe"
    print(two_subserquence(s1, s2))