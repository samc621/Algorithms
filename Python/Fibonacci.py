def fibonacci(depth):
    lastIndex = 0
    newIndex = 1
    phi = []

    phi.append(lastIndex)
    phi.append(newIndex)
    for i in range(2, depth):
        result = lastIndex + newIndex
        phi.append(result)
        lastIndex = newIndex
        newIndex = result
    print(phi)


fibonacci(10)
