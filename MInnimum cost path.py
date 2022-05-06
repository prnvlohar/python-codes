def cost(matrix):
    count=0
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0]*m for i in range(n)]
    dp[0][0] = matrix[0][0]
    for j in range(1, m):
        count+=1
        dp[0][j] = matrix[0][j] + dp[0][j-1]
    for i in range(1, n):
        count+=1
        dp[i][0] = matrix[i][0] + dp[i-1][0]
    for i in range(1, n):
        for j in range(1, m):
            count+=1
            dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])
    print(dp)
    return (dp[n-1][m-1]-matrix[n-1][m-1])

k=[[ 1,12,1,1,1 ],[ 1,1,1,23,1],[15,14,16,12,1],[45,12,56,23,1]]            
print(cost(k))
