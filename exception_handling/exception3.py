file = ''
try:
    file = open('./demofile.txt','r')
    print(file.read())
except FileNotFoundError :
    print('error : cant find file or read data')
else:
    print('no exception occured')
finally:
    print('this block is always executed')
