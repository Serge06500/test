p = int(input())
q = int(input())

k=0
for i in range(p, q+1):
    for j in range(i, q+1):
        mn = min(i + j-1, q)
        if mn >= j:
            k += mn - j + 1
print(k)
