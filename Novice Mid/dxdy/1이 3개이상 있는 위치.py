'''
숫자 0과 1로만 이루어진 n * n 크기의 격자 상태가 주어집니다. 각 칸 중 상하좌우로 인접한 칸 중 숫자 1이 적혀 있는 칸의 수가 3개 이상인 곳의 개수를 세는 프로그램을 작성해보세요. 단, 인접한 곳이 격자를 벗어나는 경우에는 숫자 1이 적혀있지 않은 것으로 생각합니다.

입력 형식
첫 번째 줄에 n이 주어집니다.

두 번째 줄부터는 n개의 줄에 걸쳐 각 줄마다 각각의 행에 해당하는 n개의 숫자가 공백을 사이에 두고 주어집니다. 전부 0과 1로 이루어져 있다고 가정해도 좋습니다.

1 ≤ n ≤ 100
'''

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def adj_cnt(x,y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx,ny) and arr[nx][ny] == 1:      
            # and는 두 조건 중 하나만 거짓이면 바로 거짓이기에 순서가 중요하다. in_range함수가 참인 경우에만 a[nx][ny]를 확인
            cnt += 1
    return cnt

total = 0
for i in range(n):
    for j in range(n):
        if adj_cnt(i,j) >= 3:
            total += 1


print(total)