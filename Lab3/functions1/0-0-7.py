def spy_game(nums):
    pattern = [0, 0, 7]
    idx = 0
    for i in nums:
        if i == pattern[idx]:
            idx += 1
        if idx == len(pattern):
            return True  
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
            
        
    