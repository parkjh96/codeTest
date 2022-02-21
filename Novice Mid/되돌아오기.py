'''
되돌아오기
(0, 0)에서 시작하여 총 N번 움직여보려고 합니다. N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어지고, 1초에 한 칸씩 움직인다고 했을 때, 몇 초 뒤에 처음으로 다시 (0, 0)에 돌아오게 되는지를 판단하는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에 정수 N이 주어집니다.

두 번째 줄부터는 N개의 줄에 걸쳐 각 줄마다 이동방향과 이동한 거리가 공백을 사이에 두고 주어집니다. 방향은 W, S, N, E중에 하나이며 각각 서, 남, 북, 동쪽으로 이동함을 의미합니다.

1 ≤ N ≤ 100
1 ≤ 한 번에 움직이는 거리 ≤ 10
출력 형식
첫 번째 줄에 다시 시작점으로 되돌아오는 데 걸리는 시간을 출력합니다. 만약 N번 이동을 진행했는데도 시작점으로 돌아오지 못했다면 -1을 출력합니다.
'''

n = int(input())

x, y = 0,0 #initial 좌표

dx = [1,-1,0,0] #동서
dy = [0,0,-1,1] #남북

mapper = {
    "E" : 0,
    "W" : 1,
    "S" : 2,
    "N" : 3
}

   #변수 초기화 위치 for문 밖
reachable = False

def simulate():
    global x, y
    time = 0 
    for _ in range(n):
        c_dir, dist = tuple(input().split())
        dist = int(dist)

        move_dir = mapper[c_dir]

        for _ in range(dist):
            time += 1
            x += dx[move_dir]
            y += dy[move_dir]

            if x == 0 and y==0:
                return time
                #sys.exit(0) 프로그램을 끝내버림 or quit()
    return -1

print(simulate())


# if not reachable:       # n번 도는 for문에서, 0,0에서 안끝남
#     print(-1)



#포인트1 if reach == False 는 대게 ==> if not 으로 쓰인다. 반대로 True는 if 변수: 이런식으로 사용

#포인트2 break는 가장 가까이에 있는 for loop을 완전히 탈출한다. 즉 이중 for loop의 경우 바깥 for는 끝나지 않음.