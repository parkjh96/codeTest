n = input()
x, y = 0,0 #initial 좌표
cur_dir = 3
dxs = [1,0,-1,0] #동서
dys = [0,-1,0,1] #남북
dest = False

def simulate():
    global x, y, cur_dir, n
    for i in range(len(n)):
        move_dir = n[i]
        if move_dir == 'L':
            cur_dir = (cur_dir - 1 + 4) % 4
        elif move_dir == 'R':
            cur_dir = (cur_dir + 1) % 4
        else:
            x, y = x +dxs[cur_dir], y + dys[cur_dir]
        if x==0 and y ==0:
            print(i+1)
            dest = True
            break

    return -1

simulate()