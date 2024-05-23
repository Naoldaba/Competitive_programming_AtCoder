N=int(input())
days=[]
for _ in range(N):
    activities=list(map(int, input().split()))
    days.append(activities)

dp=[[0, 0, 0] for j in range(N)]

dp[0][0]=days[0][0]
dp[0][1]=days[0][1]
dp[0][2]=days[0][2]

for i in range(1, N):
    dp[i][0]=days[i][0]+max(dp[i-1][1], dp[i-1][2])
    dp[i][1]=days[i][1]+max(dp[i-1][0], dp[i-1][2])
    dp[i][2]=days[i][2]+max(dp[i-1][0], dp[i-1][1])

print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2]))
