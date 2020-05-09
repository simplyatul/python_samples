# unordered, changable, indexed w/ no duplicate members

session = {
  'id':'xyz123',
  'from': 'abc',
  'to': 'pqr'
}

print(session)  # {'id': 'xyz123', 'from': 'abc', 'to': 'pqr'}
print(type(session)) # <class 'dict'>

# Using C'tor
session = dict(id='xyz123', from1='abc', to1='pqr') 
# from and to looks reserved keywords. Python throwing error. So using form1 and to1 

print(session)  # {'id': 'xyz123', 'from1': 'abc', 'to1': 'pqr'}
print(type(session)) # <class 'dict'>


print(session['id'])  # xyz123

# Adds new kv pair

session['via'] = 'ip1'
print(session) # {'id': 'xyz123', 'from1': 'abc', 'to1': 'pqr', 'via': 'ip1'}

# Get only Keys
print(session.keys()) # dict_keys(['id', 'from1', 'to1', 'via'])
print(type(session.keys())) # <class 'dict_keys'>

# Get only Values
print(session.values()) # dict_values(['xyz123', 'abc', 'pqr', 'ip1'])

print(type(session.values())) # <class 'dict_values'>

# Get all elements in Dict
print(session.items())  # dict_items([('id', 'xyz123'), ('from1', 'abc'), ('to1', 'pqr'), ('via', 'ip1')])

# Remove an iteam

del(session['via'])
print(session.items()) # dict_items([('id', 'xyz123'), ('from1', 'abc'), ('to1', 'pqr')])






