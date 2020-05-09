print('Concat' + ' String')

print('{}, {}, {}'.format('a', 'b', 'c')) # a, b, c

# Position the arguments
print('{1}, {2}, {0}'.format('a', 'b', 'c')) # b, c, a
# print('{1}, {2}, {9}'.format('a', 'b', 'c')) # IndexError: Replacement index 9 out of range for positional args tuple

# Args by name
city = 'XYZ'
print('Hi, I am {name} and I live in {c} city'.format(name='Mr. X', c=city))

n = 'Mr. X'
# F-Strings (v3.6+)
print(f'Hi, I am {n} and I live in {city} city')
