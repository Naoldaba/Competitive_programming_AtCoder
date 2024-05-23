N = int(input())
arr = list(map(int, input().split()))

arr.insert(0, 0)

dp = [0] * (N + 1)
dp[2] = abs(arr[2]-arr[1])

for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + abs(arr[i] - arr[i - 1]), dp[i - 2] + abs(arr[i] - arr[i - 2]))

print(dp[N])
