from pprint import pprint

name = 'sample2.txt'
file = open(name, 'r')  # open file  # r - read, w - write, a - append
# pprint(file.read())  # read all
# file.write('hello')  # write
pprint(file.tell())
pprint(file.read())
pprint(file.seek(20))
pprint(file.read())
file.close()  # close file
