num = 5

def g():
    print(num, end=" ")

def f():
    num = 9
    while num < 8:
        num += 1
    print(num, end=" ")
    g()

f()

print(num, end=" ")