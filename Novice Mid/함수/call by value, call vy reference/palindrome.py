A = input()

def is_palindrome(string):
    for i in range(len(string)):
        if string[i] != string[len(string) - i- 1]:
            return False
    return True

if is_palindrome(A):
    print("Yes")
else: print("No")


# return 값을 False로 할지 True로 할지는 원하는 출력값에 따라 조정해야한다.