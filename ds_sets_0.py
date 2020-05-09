# Set: unordered (=> unindex). No duplicate members

nums = {12,20,3,4, 4}
print(type(nums)) # <class 'set'> 
print(nums) # {4, 3, 12, 20}

# unindex
# print(nums[1]) # TypeError: 'set' object is not subscriptable:w

nums.add(99) 
print(nums) # {99, 4, 3, 12, 20}

nums.clear()
print(nums) # set()

del nums
# print(nums) # NameError: name 'nums' is not defined
