def fibonacci(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    if (n > 1):
        i = 1
        f_1 = 1
        f_2 = 0
        f = 0
        while i < n:
            f = f_1 + f_2
            f_2 = f_1
            f_1 = f
            i += 1
        return f

n = int(input("Podaj numer wyrazu w ciągu: "))
print (fibonacci(n))
