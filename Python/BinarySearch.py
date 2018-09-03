from random import randint

min = 1
max = 100000000
lowerBound = min
higherBound = max

number = randint(min, max)

count = 1


def binarySearch(guess):
    global count
    global lowerBound
    global higherBound
    if (guess > number):
        higherBound = guess
        count += 1
        binarySearch(round((lowerBound + higherBound) / 2))
    elif (guess < number):
        lowerBound = guess
        count += 1
        binarySearch(round((lowerBound + higherBound) / 2))
    elif (guess == number):
        print("The answer is " + str(int(guess)) + ".")
        print("This took " + str(count) + " tries.")


binarySearch(round(max / 2))
