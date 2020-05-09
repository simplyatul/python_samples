# Tuples: Ordered (=> can indexed) and unchangable/immutable. Allows Duplicates  

nums = (12,20,3,4, 4)
print(type(nums)) # <class 'tuple'>

# One other way
nums = tuple((33, 9, 88, 0, 9))
print(type(nums)) # <class 'tuple'>

print(nums[1]) # 9

# Immutable: Can not change value 
# nums[1] = 100 # TypeError: 'tuple' object does not support item assignment

# Tuples with one value should have trailing comma
nums = (1)
print(type(nums)) # <class 'int'>

nums = (1,)
print(type(nums)) # <class 'tuple'>

# Immutable but can delete the tuple 
del nums
print(type(nums))

