result = True


def Palindrome(word):
    global result
    max = len(word)
    for i in range(1, max+1):
        if word[i-1] != word[max-i]:
            result = False
    print(result)


Palindrome("ayya")
