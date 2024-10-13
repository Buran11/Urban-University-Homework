# a = 'Hello, World!'  # ASCII(127) UNICODE(65533)
# chars = []
# for i in a:
#     chars.append(ord(i))
# print(chars)
# s = ''
# for i in chars:
#     s += chr(i)
# print(s)

print(hex(ord('h')))
bb = b'\x68'
print(bb.decode())
