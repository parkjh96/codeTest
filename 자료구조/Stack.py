class Stack:
    def __init__(self):
        self.items = [ ]
        
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

S = Stack()
for p in parseq:
    if p == ‘(’ :
        S.push(p)
    elif p == ‘)’:
        S.pop()
    else: print(”Not allowed Symbol”)
if len(S) > 0:
    return False
else: return True