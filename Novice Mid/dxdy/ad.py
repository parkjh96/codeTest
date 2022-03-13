offset = 100
max_r = 100

a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))
sum_val = 0
arr = [0] * (max_r + 1)


def fill_arr(x,y):
    global sum_val
    for i in range(x,y):
        if arr[i] > 0:
            continue
        arr[i] += 1
        sum_val += 1
    return arr


fill_arr(a,b)
fill_arr(c,d)
print(sum_val)
