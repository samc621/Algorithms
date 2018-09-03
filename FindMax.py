def findMax(list):
    result = 0
    for i in range(0, len(list)):
        if (list[i] > result):
            result = list[i]
    print(result)


findMax([1, 2, 18, 40, 6, 10])
