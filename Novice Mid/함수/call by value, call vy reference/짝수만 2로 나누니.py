n = int(input())

arr = list(map(int, input().split()))


def div_by_two(arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
    return arr[i]

div_by_two(arr)

for elem in arr:
    print(elem, end=" ")


## list는 mutable하다. 함수로 들어가서 반환하면 본래의 list가 바뀌는 것을 기억하자.