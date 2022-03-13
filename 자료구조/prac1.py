import random, time

def evaluate_n(A, x):
    n = int(input())
    A = [ random.randint(-1000,1000) for _ in range(n)]
    e = time.process_time()
    print(A)
    print("수행시간 =" , e)



A1 = []
x1 = int
random.seed()
evaluate_n(A1,x1)


# n = int(input())
# # 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
# random.seed()
# # 다항식의 계수를 저장한 리스트
# A = [
#     random.randint(-1000,1000)
#     for _ in range(n)
# ]

# e = time.process_time()
# print("수행시간 =" , e)

# print(A)