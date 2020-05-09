# List => is a collection/array. Ordered (=> can indexed) and changable/mutable. Allows duplicates  
# Generally contains same type of objects, but it supports mutiple type of objects packed

nums = [12,20,3,4, 4]
print(type(nums)) # <class 'list'>

# One other way
nums = list((33, 9, 88, 0, 9))
print(type(nums)) # <class 'list'>

print(nums[1])  # 9 

nums.append(39)
print(nums)
print(nums.reverse()) # None
print(nums) 

nums.sort(reverse=True)
print(nums) 
