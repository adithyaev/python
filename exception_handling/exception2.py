try:
    a = int(input('enter a number : '))
    result = 10 / a
    print('result is ',result)
except ZeroDivisionError as e:
    print('error : division by zero')
except ValueError as e:
    print('erraor : invalid input')
else:
    print('no exceptions occured. everything executed succesfully')
finally:
    print('this block is always executed')