def aggregate(x, y):
    if x > y:
        x += 25
        y *= 2
    else: 
        y += 25
        x *= 2
    return x, y

a, b = tuple(map(int, input().split()))

a, b = aggregate(a,b)
print(a, b)


#변수 지정 순서도 중요