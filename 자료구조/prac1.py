import time, random

random.seed()
n = int(input())
A = [random.randint(-1000,1000) for _ in range(n)]
print(A)