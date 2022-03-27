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


def infix_to_postfix(infix):
    opstack = Stack()   #괄호와 연산자 저장
    outstack = []       # postfix수식을 저장하기 위한 리스트
    token_list = infix.split(" ")      #input인 infix 입력값을 스플릿하여 토큰화

    #연산자의 우선순위 설정 ( ^ * / + - 순
    prec = {}
    prec['('] = 0
    prec['^'] = 3
    prec['*'] = 2
    prec['/'] = 2
    prec['+'] = 1
    prec['-'] = 1

    for token in token_list:
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


infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)


