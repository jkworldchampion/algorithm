import sys

n = int(sys.stdin.readline())
dp = [0]

for _ in range(n):
    x = int(sys.stdin.readline())
    if (x >= len(dp)):
        dp = [0] * (x+1)
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2
        for i in range(6, x+1):
            dp[i] = dp[i-5] + dp[i-1]
    print(dp[x])
