
n, k = map(int, input().split())
arr=list(map(int, input().split()))

dp=[float('inf')]*n
dp[0]=0

for i in range(n):
    for j in range(i-1, max(i-1-k, -1), -1):
        dp[i]=min(dp[i], dp[j]+abs(arr[i]-arr[j]))

print(dp[n-1])
