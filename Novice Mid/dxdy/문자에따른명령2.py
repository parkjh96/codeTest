'''
좌표평면 위 (0, 0)에서 북쪽을 향한 상태에서 움직이는 것을 시작하려 합니다. N개의 명령에 따라 총 N번 움직이며, 명령 L이 주어지면 왼쪽으로 90도 방향 전환을, 명령 R이 주어지면 오른쪽으로 90도 방향전환을 하고, 명령 F가 주어지면 바라보고 있는 방향으로 한칸 이동하려고 합니다. 이동 이후 최종 위치를 출력하는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에 문자 ‘L', ‘R', 그리고 'F’로만 이루어진 문자열이 하나 주어집니다.

1 ≤ 명령의 길이 ≤ 100,000
'''

orders = input()

dir_num = 3 
x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

#dir_num = (dir_num + 1) % 4 #시계방향
# dir_num = (dir_num - 1 + 4) % 4 # 반시계방향

for order in orders:
    if order == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif order == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]


print(x, y)