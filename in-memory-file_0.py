from io import StringIO

output = StringIO()
output.write('First line.\n')
output.write('Second line.\n')

print('File Contents: ', output.getvalue())
output.close()
