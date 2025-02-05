from itertools import permutations

def perms(s):
    perm_list = permutations(s)
    for perm in perm_list:
        print(''.join(perm))

word = input("Enter a string: ")
perms(word)
