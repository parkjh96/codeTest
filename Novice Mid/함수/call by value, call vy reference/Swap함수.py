'''
Python에서는 변수의 type에 따라 immutable과 mutable한 것으로 나뉩니다. 대표적으로 immutable한 type에는 tuple, string 그리고 int, bool 등을 포함한 primitive type들이 있고, mutable한 type에는 list, dict 등이 있습니다.

immutable 특성을 갖는 변수가 함수의 인자로 넘어가게 되면, 변할 수 없는 특성 때문에 그 변수가 그대로 넘어가는 것이 아닌, 변수가 갖고 있던 값을 복사하여 값을 넘겨주게 됩니다.

즉, 이 코드에서는 immutable한 int형 변수인 n, m이 함수 인자로 넘어가게 된 경우이므로, 변수 자체가 swap 함수로 넘어간 것이 아닌, n, m에 적혀있었던 값이 a, b에 복사가 되어 넘어가게 된 것입니다. 함수 안에서 a, b 값은 바뀌게 되어 첫 번째 출력 결과는 20 10이 나오게 되었지만, 함수를 빠져나오게 되었을 때, n, m 값에는 전혀 변화가 없었으므로 n, m 출력 결과는 그대로 10 20이 나오게 됩니다.

immutable - call by value (int, str, tuple, bool) -> 무조건 변수가 갖고 있던 값을 복사하여 값 자체를 넘겨줌
mutable - call by reference (list, dict)    -> 참조를 넘겨줄 수 있다. 주소를 넘겨줌

def swap(a, b):
    a, b = b, a
    return a, b
    
**함수 밖에서 영향을 미치려면 return으로 값을 넘겨주어야한다**

n, m = 10, 20
n, m = swap(n, m)
print(n, m)

>> 20 10
'''

n, m = tuple(map(int, input().split()))

def swap(a, b):
    a , b = b, a
    return a, b

n, m = swap(n, m)
#int는 immutable하기 때문에 변수 초기화를 새로 해줘야한다.
print(n, m)