n = int(input())
arr = [int(input()) for i in range(n)]
arr = sorted(arr)
s = 0
for i in range(len(arr) - 1):
    s += arr[i] + 1
s += 2
print(s)