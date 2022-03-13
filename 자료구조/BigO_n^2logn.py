def algorithm_doSomething(n):
    count = 0
    for i in range(n):
        for j in range(n):
            k = 1
            while k < n:
                count += 1
                k = k * 2
    return count


print(algorithm_doSomething(100))