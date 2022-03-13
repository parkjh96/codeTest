import time, random



# def evaluate_n2(A, x):
	# code for O(n^2)-time function
	
# def evaluate_n(A, x):
# 	# code for O(n)-time function
	
random.seed()		# random 함수 초기화
# n 입력받음
n = int(input())
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = [
    random.randint(-1000,1000)
    for _ in range(n)
]
# evaluate_n2 호출
# evaluate_n 호출
# 두 함수의 수행시간 출력