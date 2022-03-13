'''
time 모듈 perf_counter와 process_time의 차이
perf_counter는 코드 연산 시간 외에 sleep, file io 등 pending에 들어가는 시간까지 모두 포함해서 측정

process_time은 코드의 연산 시간만을 측정 pending 시간은 측정되지 않는다.
'''

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