t = int(input())
n = int(input())
ttc = 0
k = 0
curt = 0
timeline = [int(input()) for i in range(t)]
paths = [int(input()) for i in range(n)]

for i in range(1, len(timeline) + 1):
    if ttc + paths[timeline[i - 1] - 1] <= i - curt:
        k+=1
        ttc = paths[timeline[i - 1] - 1]
        curt = i
    else: pass

print(k)
    