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




def compute_postfix(postfix):
    opstack = Stack()
    token_list = postfix.split(" ")

    for token in token_list:
        if token in "+-*/^":
            if token == "+":
                num1 = opstack.pop()
                num2 = opstack.pop()
                opstack.push(num2 + num1)
            elif token == "-":
                num1 = opstack.pop()
                num2 = opstack.pop()
                opstack.push(num2 - num1)
            elif token == "*":
                num1 = opstack.pop()
                num2 = opstack.pop()
                opstack.push(num2 * num1)
            elif token == "/":
                num1 = opstack.pop()
                num2 = opstack.pop()
                opstack.push(num2 / num1)
            elif token == "^":
                num1 = opstack.pop()
                num2 = opstack.pop()
                opstack.push(num2 ** num1)

        else:
            opstack.push(float(token))

    return float(opstack.pop())





postfix_expr = input()
postfix_compute = compute_postfix(postfix_expr)
print(postfix_compute)
