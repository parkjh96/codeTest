class myList():
    def __init__(self):
        self.capacity = 2
        self.n = 0
        self.A = [None] * self.capacity     #[none, none]을 가진 배열 A
    
    def __len__(self):
        return self.n
    
    def __str__(self):
        return f'({self.n}/{self.capacity}): ' + '[' + ', ' .join([str(self.A[i]) for i in range(self.n)]) + ']'

    def __getitem__(self, k): # k번째 칸에 저장된 값 리턴
        # k가 음수일 수도 있음
        if k < 0:
            k += self.n
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
        if (k < 0) or (k >= self.n):
            raise IndexError
        return self.A[k]        #밑의 while문에서 A[k] -> cmd[n] 쓰이고 있음

    def __setitem__(self, k, x): # k번째 칸에 값 x 저장
		# k가 음수일 수도 있음
        if k < 0:
            k += self.n
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
        if (k<0) or (k >= self.n):
            raise IndexError
        self.A[k] = x
    def insert(self, k, x):
		# 주의: k 값이 음수값일 수도 있음
        if k < 0:
            k += self.n
		# k 값이 올바른 인덱스 범위를 벗어나면, raise IndexError
        if (k < 0) or (k >= self.n):
            raise IndexError
		# 1. k의 범위가 올바르지 않으면 IndexError 발생시킴
		# 2. self.n == self.capacity이면 self.change_size(self.capacity*2) 호출해 doubling
        if self.capacity >= 4 and self.n <= self.capacity//4: # 실제 key 값이 전체의 25% 이하면 halving
            self.change_size(self.capacity*2)
		# 3. A[k]와 오른쪽 값을 한 칸씩 오른쪽으로 이동
        for i in range(self.n, k-1, -1):
            self.A[i] = self.A[i-1]
        self.A[k] = x
        self.n += 1
		# 4. self.A[k] = x
		# 5. self.n += 1
	
    def size(self):
        return self.capacity

A = [1,2,3,4,5]
A = myList()
A.insert(1,5)
print(A)