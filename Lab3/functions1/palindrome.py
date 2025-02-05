def ispalindrome(word):
    if word == word[::-1]:
        return True
    return False

word = input("enter the word: ")
print(ispalindrome(word))
    