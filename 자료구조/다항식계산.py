import time, random
		
def evaluate_n2(A, x):
    sumval = 0                  #대입연산 +1
    temp = 0                    #대입연산 +1
    global n
    for i in range(0,n):        #to n-1
        temp = A[i]             #대입연산 +1
        for _ in range(i):      #to n-1
            temp = temp * x     #대입+산술 +2 두번째 for문
        sumval = temp + sumval  #대입+산술 +2 첫번째 for문
    return sumval               # 2 + (3n-3)*(2n-2) = 6n^2-12n+8 =O(n^2)

def evaluate_n(A, x):
    global n
    sumval = 0                  #대입 1회
    temp = 0                    #대입 1회
    for i in range(n):          #to n-1
        temp = A[i] * (x**i)    #대입+산술2 = +3
        sumval += temp          #대입+산술 +2
    return sumval               # 2 + 5(n-1) = 5n-3 = O(n)
	
# random 함수 초기화
random.seed()
# n 입력받음
n = int(input())
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = [random.randint(-1000,1000) for _ in range(n)] #랜덤정수 n개 생성한 리스트 컴프리헨션
x = random.randint(-1000,1000)

print("evaluate_n2")
before = time.process_time()    #함수 이전시간
print("before = ", before)
evaluate_n2(A,x)                #O(n^2) 호출
after = time.process_time()     #함수 이후시간
print("after = ", after)
print("after - before = ", after - before)

print("------------------------------")

print("evaluate_n")
before = time.process_time()    #함수 이전시간
print("before = ", before)
evaluate_n(A,x)                 #O(n) 호출
after = time.process_time()     #함수 이후시간
print("after = ", after)
print("after - before = ", after - before)