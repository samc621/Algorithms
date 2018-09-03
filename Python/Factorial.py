def Factorial(num):
    result = num
    for i in range(1, num):
        result *= num-i
    print(result)


Factorial(5)
