
myFile = open('myfile.txt', 'w')

print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

myFile.write('Hello myfile')
myFile.close()

