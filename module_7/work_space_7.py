import os

print('Текущая директория: ', os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('Текущая директория: ', os.getcwd())
print(os.listdir())
for i in os.walk(os.getcwd()):
    print(i)
os.chdir(r'C:\Users\sysman\Desktop\Urban\test\second')
print('Текущая директория: ', os.getcwd())
print(os.listdir())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
# os.startfile(file[0])
# print(os.stat(file[0]).st_size)
os.system('cls')
