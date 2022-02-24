def isPalindrome(str):
    strLen = len(str)

    for x in range(0, int(strLen/2), 1):
        if(str[x] != str[strLen-(x+1)]):
            return False
    return True

def fibFunc(n):
    if(int(n) <= 0):
        print("Please enter an integer greater than 0!")
        return

    prev = 0
    curr = 1

    print("Count 1: " + str(curr))

    for x in range(1, int(n), 1):
        print("Count " + str((x+1)) + ": " + str((prev + curr)))
        temp = prev
        prev = curr
        curr = curr + temp

userIn = input("Enter a word: ")
palindrome = isPalindrome(userIn)
if (palindrome):
    print("This is a palindrome")
else:
    print("This is not a palindrome")

numPalin = input("How many terms: ")
fibFunc(numPalin)
