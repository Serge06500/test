a = int(input())
h = int(input())
k = int(input())
m = int(input())
s = int(input())

def ceil(x):
        return int(x) if x == int(x) else int(x) + 1

print(ceil(ceil(a / m) / (s // (ceil(h / k) * k))))