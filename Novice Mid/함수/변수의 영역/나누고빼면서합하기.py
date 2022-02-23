n, m = tuple(map(int, input().split()))
A = [0] + list(map(int, input().split())) ##A[m]의 값이 한칸씩 밀리기 떄문에 인덱스에 0을 넣어준다

def aggregate():
    global m
    ans = 0

    while m:
        ans += A[m]

        if m%2 == 0:
            m //= 2
        else: m -= 1
    return ans

print(aggregate())
