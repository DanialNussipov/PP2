def unique_elements(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

numbers = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8]
result = unique_elements(numbers)
print(result)
