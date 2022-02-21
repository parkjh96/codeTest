_list = [1, 2, 3, 4]

def sum_all(arr):
    sum_val = 0
    for elem in arr:
        sum_val += elem

    return sum_val


total_sum = sum_all(_list)
print(total_sum)

'''
함수 위에 값들을 정의하게 되면, 어디에서도 쓰일 수 있는 global 변수가 되기 때문에, sum_all 함수 안에서 _list 값을 바로 참조할 수 있게 됩니다.
'''
_list = [1, 2, 3, 4]


def sum_all():
    sum_val = 0
    for elem in _list:
        sum_val += elem

    return sum_val


total_sum = sum_all()
print(total_sum)
