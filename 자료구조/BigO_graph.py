import matplotlib.pyplot as plt
import time, random
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

def prefixSum1(X, n):
    S = [0] * n
    for i in range(n):
        S[i] = 0
        for j in range(i+1):
            S[i] += X[j]


def prefixSum2(X, n):
	# code for prefixSum2
    S = [0] * n
    S[0] = X[0]
    for i in range(n):
        S[i] = S[i-1] + X[i]

random.seed()
# # random_num = random.randint(-999,999)
# #print(random_num)
# n= int(input())
# X1 = [0] * n
# for elem in range(n):
#     X1[elem] = random.randint(-1000,1000)
#     # print(X1[elem])

# print("prefixSum1")
# before1 = time.process_time()
# print("before = ", before1)
# prefixSum1(X1,n)
# after1 = time.process_time()
# print("after = ", after1)
# result1 = after1 - before1
# print("after - before = ", result1) 

m = int(input())
list1 = []
list2 = []
for i in range(m):
    n = int(input())
    X1 = [0] * n
    for elem in range(n):
        X1[elem] = random.randint(-1000,1000)

    print("prefixSum1")
    before1 = time.process_time()
    print("before = ", before1)
    prefixSum1(X1,n)
    after1 = time.process_time()
    print("after = ", after1)
    result1 = after1 - before1
    list1.append(result1)
    print("after - before = ", result1)

    print("=============================================")   

    print("prefixSum2")
    before2 = time.process_time()
    print("before = ", before2)
    prefixSum2(X1,n)
    after2 = time.process_time()
    print("after = ", after2)
    result2 = after2 - before2
    list2.append(result2)
    print("after - before = ", result2) 



# print("=============================================")
# print("prefixSum2")
# before2 = time.process_time()
# print("before = ", before2)
# prefixSum2(X1,n)
# after2 = time.process_time()
# print("after = ", after2)
# result2 = after2 - before2
# print("after - before = ", result2)

plt.plot(list1, label= "O(n^2)")
plt.xticks([0, 1, 2, 3], labels=["1000","5000","10000","20000"])
plt.plot(list2, label= "O(n)")
plt.xticks([0, 1, 2, 3], labels=["1000","5000","10000","20000"])
plt.xlabel('n값')
plt.ylabel('시간 (초)')
# # plt.xlim([0,100000])
# # plt.ylim([0,3])
plt.legend()
plt.show()

