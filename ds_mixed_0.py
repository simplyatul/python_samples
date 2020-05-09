# list of dictionary

sessions = [
  {'id':'xyz111',
  'from': 'abc',
  'to': 'pqr'},
  {'id':'xyz222',
  'from': 'pqr',
  'to': 'abc'},

]

print(sessions) # [{'id': 'xyz111', 'from': 'abc', 'to': 'pqr'}, {'id': 'xyz222', 'from': 'pqr', 'to': 'abc'}]

print(sessions[1]['id'])  # xyz222

