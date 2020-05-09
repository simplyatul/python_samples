def sayHi(Hi):
  """
  This is the function doc help
  Prints Hi
  Returns X
  """
  Hi = 'Bye'
  print(Hi)

say = 'Hello'
sayHi(say) # passes param by value

print(say)

# Lambda functions

getSum = lambda n1, n2: n1+n2
print(getSum(23, 10))
