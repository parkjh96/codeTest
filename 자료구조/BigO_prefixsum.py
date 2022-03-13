import time, random

def prefixSum1(X, n):
    print("prefixSum1")
    S = [0] * n
    for i in range(n):
        S[i] = 0
        for j in range(i+1):
            S[i] += X[j]


def prefixSum2(X, n):
	# code for prefixSum2
    print("prefixSum2")
    S = [0] * n
    S[0] = X[0]
    for i in range(n):
        S[i] = S[i-1] + X[i]

random.seed()
# random_num = random.randint(-999,999)
#print(random_num)
n= int(input())
X1 = [0] * n
for elem in range(n):
    X1[elem] = random.randint(-999,999)
    # print(X1[elem])

# print(X1)
# print(prefixSum1(X1,n))
before = time.process_time()
print("before = ", before)
prefixSum1(X1,n)
after = time.process_time()
print("after = ", after)
print("after - before = ", after - before) 

before = time.process_time()
print("before = ", before)
prefixSum2(X1,n)
after = time.process_time()
print("after = ", after)
print("after - before = ", after - before) 