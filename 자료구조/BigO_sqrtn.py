def algorithm_doSomething(n):
    count = 0
    k = 1
    while k*k <= n:
        count += 1
        k += 1
    return count


print(algorithm_doSomething(100))