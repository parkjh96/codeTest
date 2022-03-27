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


def infix_to_postfix(infix):
    opstack = Stack()   #괄호와 연산자 저장
    outstack = []       # postfix수식을 저장하기 위한 리스트
    #token_list = infix.split(" ")      #input인 infix 입력값을 스플릿하여 토큰화

    #연산자의 우선순위 설정 ( ^ * / + - 순
    prec = {}
    prec['('] = 0
    prec['^'] = 3
    prec['*'] = 2
    prec['/'] = 2
    prec['+'] = 1
    prec['-'] = 1

    for token in infix:
        if token == "(":                                                 #"(" 이면 무조건 push
            opstack.push(token)
        elif token == ")":
            while opstack.top() != "(":                                        #opstack 내에 '(' 가 나올때 까지 pop과 동시에 oustack에 append
                outstack.append(opstack.top())
                opstack.pop()
            opstack.pop()                                                      # '(' 제거
        elif token in "^*/+-":
            if opstack.isEmpty():                                              #S이 비어있으면 token push
                opstack.push(token)
            elif prec[opstack.top()] >= prec[token]:                           #우선순위가 낮으면 push
                while not opstack.isEmpty() and prec[opstack.top()] >= prec[token]:  #높은 우선순위 pop
                    outstack.append(opstack.top())
                    opstack.pop()
                opstack.push(token)                                            #우선순위 연산자를 모두 pop하고 자신이 push
            else: opstack.push(token)                                          #연산자의 우선순위가 낮은 경우
        else:                                                            #피연산자 라면
            outstack.append(token)

    while not opstack.isEmpty():                                               #위의 연산이 끝나고 S에 있는 모든 연산자 pop할 때 까지
        outstack.append(opstack.top())
        opstack.pop()
    
    return " ".join(outstack)

def compute_postfix(postfix):
    opstack = Stack()
    outstack = []
    token_list = postfix.split(" ")

    for token in token_list:
        if token in "+-*/^":
            if token == "+":
                num1 = opstack.pop()
                num2 = opstack.pop()
                opstack.push(num2 + num1)
            elif token == "-":                  #두번째 pop값에서 첫번째 pop값을 뺴야함
                num1 = opstack.pop()
                num2 = opstack.pop()
                opstack.push(num2 - num1)
            elif token == "*":
                num1 = opstack.pop()
                num2 = opstack.pop()
                opstack.push(num2 * num1)
            elif token == "/":                  #두번째 pop값에서 첫번째 pop값을 나눠야함
                num1 = opstack.pop()
                num2 = opstack.pop()
                opstack.push(num2 / num1)
            elif token == "^":                  #두번째 pop값에서 첫번째 pop값을 제곱해야함
                num1 = opstack.pop()
                num2 = opstack.pop()
                opstack.push(num2 ** num1)

        else:                                   #피연산자이면
            opstack.push(float(token))          #float으로 변환한 후 push

    for result in opstack.items:
        answer = result

    return answer




expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)

# 3+ 2* 4/(6- 1)
# 3.14*2.10/(10.2-21)