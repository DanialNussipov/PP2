thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

