import matplotlib.pyplot as plt
import time, random
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

def evaluate_n2(A, x):
    sumval = 0
    temp = 0
    global n
    for i in range(n):
        temp = A[i]
        for j in range(i):
            temp = temp * x
        sumval = temp + sumval
    return sumval


def evaluate_n(A, x):
    global n
    sumval = 0
    temp = 0
    for i in range(n):
        temp = A[i] * (x**i)
        sumval += temp
    return sumval

random.seed()

m = int(input())
list1 = []
list2 = []
for i in range(m):
    n = int(input())
    A = [random.randint(-1000, 1000) for _ in range(n)]
    x = random.randint(-1000, 1000)

    print("evaluate_n2")
    before1 = time.process_time()
    print("before = ", before1)
    evaluate_n2(A,n)
    after1 = time.process_time()
    print("after = ", after1)
    result1 = after1 - before1
    list1.append(result1)
    print("after - before = ", result1) 

    print("evaluate_n")
    before2 = time.process_time()
    print("before = ", before2)
    evaluate_n(A,n)
    after2 = time.process_time()
    print("after = ", after2)
    result2 = after2 - before2
    list2.append(result2)
    print("after - before = ", result2)
    print("=============================================")  


plt.plot(list1, label= "O(n^2)")
plt.xticks([0, 1, 2, 3], labels=["1000","5000","10000","15000"])
plt.plot(list2, label= "O(n)")
plt.xticks([0, 1, 2, 3], labels=["1000","5000","10000","15000"])
plt.xlabel('n값')
plt.ylabel('시간 (초)')
# # plt.xlim([0,100000])
# # plt.ylim([0,3])
plt.legend()
plt.show()

