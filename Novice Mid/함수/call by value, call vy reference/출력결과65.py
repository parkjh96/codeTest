def f(n, a):
    t = 0
    while (n > 0):
        t = n % 10
        a[t] = a[t] + 1
        n //= 10

a = [0, 1, 2, 0]
f(1202, a)
print(a[2])