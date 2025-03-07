string = input("Enter a string: ")
reversed_string = string[::-1]

if reversed_string == string:
    print("Is a palindrome")
else:
    print("Not a palindrome")
