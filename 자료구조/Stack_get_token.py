import string


class Stack:
    def __init__(self):
        self.items = []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    def __len__(self):
        return len(self.items)
    def isEmpty(self):
        return self.__len__() == 0


def get_token_list(expr):
    outstack = []                                               #결과 리스트
    token_list = str()
    temp_list = list(expr)

    for token in temp_list:
        if token == " ":                                        #띄어쓰기 pass
            pass
        elif token in "()+-*/^":                                #연산자를 만나면 연결해온 string을 outstack에 append, 연산자도 append
            if len(token_list) == 0:                            #대게 '('의 경우
                outstack.append(token)
            else:
                outstack.append(token_list)
                outstack.append(token)
                token_list = str()                              #스트링 초기화

        elif token == ".":                                      #위의 연산자 만나기 전까지 숫자와 (.)을 이어줌
            token_list += token
        else:
            token_list += token
    if token_list != None and token.isdecimal():                  #연산 마지막에 숫자로 끝나거나 / 연산자로끝나는 경우
        outstack.append(token_list)

    return outstack

        


expr = input()
value = get_token_list(expr)
print(value)

# 3+ 2* 4/(6- 1)
# 3.14*2.10/(10.2-21)