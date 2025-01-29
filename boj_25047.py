import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [sum(arr[j][i] for j in range(n)) for i in range(n)]

acc = arr[0][:]
WArr = [[0]*n] + deepcopy(arr)
for i in range(2, n+1):
    for j in range(n):
        WArr[i][j] -= acc[j]
    for j in range(n):
        acc[j] += arr[i-1][j]

sumcoldp = [0]*n
finalscore = 0
for i in dp:
    if i < 0:finalscore += i

for i in range(1, 1<<n-1):
    minuscore = 0
    for j in range(n):
        sumcoldp[j] += WArr[(i ^ (i-1)).bit_length()][j]
        minuscore += min(sumcoldp[j], dp[j]-sumcoldp[j])

    if finalscore < minuscore:
        finalscore = minuscore

print(finalscore)