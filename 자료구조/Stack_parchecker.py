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

def parChechker(parseq):
    S = Stack()
    for symbol in parseq:
        if symbol in "({[":
            S.push(symbol)
        elif symbol in ")}]":
            if S.isEmpty():
                #print("nothing in arr")
                return False
            #if (symbol == ")" and S.top() == "(") or (symbol == "}" and S.top() == "{") or (symbol == "]" and S.top() == "["):
            if ord(S.top()) + 1 <= ord(symbol) <= ord(S.top()) + 2:
                '''
                중괄호 {} 예시로 들자면...
                ASCII 코드 변환함수 ord("}") = 125
                현재 S.top() = "{" = 123
                ord(S.top()) = 123+1 = 124
                ord(symbol) =          125
                ord(S.top()) = 123+2 = 125
                '''
                S.pop()
        else:
            continue
    if S.isEmpty():
        return True
    else: return False

print(parChechker(input()))