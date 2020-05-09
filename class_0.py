from time import time

class Session:
  # C'Tor
  def __init__(self, id, from1, to1):
    self.id = id
    self.from1 = from1
    self.to1 = to1
    self.time = time()
  
  # def getID() # TypeError: getID() takes 0 positional arguments but 1 was given
  def getID(self):
    return self.id

  def getCreateTime(self):
    return self.time

  
s1 = Session('xy123', '123@d1.com', '1800@z.com')

# Add Property
s1.via = '555@v.com'
print(s1.id)
print(s1.via)
print(s1.getID())
print(s1.getCreateTime())

print(s1) # <__main__.Session object at 0x01207148>
