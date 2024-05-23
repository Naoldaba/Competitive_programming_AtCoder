
n, k =int(input())
arr=list(map(int, input().split()))

dp=[float('inf') for _ in range(n)]
dp[0]=0

for i in range(1, len(dp)):
    for j in range(i-1, max(i-k, -1), -1):
        dp[i]=min(dp[i], dp[j]+abs(arr[i]-arr[j]))
        
print(dp[n-1])
