import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr1, arr2 = [0] + arr[:n>>1], [0] + arr[n>>1:]
S = {0:1}

acc = arr1[int(len(arr1) > 1)]
for i in range(2, len(arr1)):
    arr1[i] -= acc
    acc += arr[i-1]

acc = arr2[1]
for i in range(2, len(arr2)):
    arr2[i] -= acc
    acc += arr[(n>>1)+i-1]

sumArr = 0
for i in range(1, 1<<(n>>1)):
    sumArr += arr1[(i ^ (i-1)).bit_length()]
    if sumArr in S:
        S[sumArr] += 1
    else:
        S[sumArr] = 1

cnt = S.get(s, 0) - int(not s)
sumArr = 0
for i in range(1, 1<<(n+1>>1)):
    sumArr += arr2[(i ^ (i-1)).bit_length()]
    cnt += S.get(s-sumArr, 0)

print(cnt)