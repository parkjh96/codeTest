def modify(arr):
    arr[0] = 10


_list = [1, 2, 3, 4]
modify(_list)

for elem in _list:
    print(elem, end=" ")

arr = [1,2,3,4,5]
arr2 = arr[:5] #5번전까지
# mutable한 list같은 경우 함수에 넣으면 주소를 넘겨주기 때문에 list의 값이 변한다. 그걸 원치 않는다면 slicing을 해주면 주소를 공유하지 않는 새로운 리스트를 만들어 마치 call by value처럼 쓸 수 있다.