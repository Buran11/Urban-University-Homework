from pprint import pprint

name = 'sample2.txt'
file = open(name, 'r', encoding='utf-8')
print(file.writable())
print(file.readable())
print(file.seekable())
print(file.buffer)
print(file.closed)
print(file.tell())

pprint(file.read())
print(file.tell())
file.close()
