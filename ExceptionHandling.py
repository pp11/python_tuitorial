a=2
b=2


try:
    print('connection open')
    print(a/b)
    i = int(input('enter a number', ))
    print(i)
except ZeroDivisionError as e:
    print('divisor can not be zero', e)
except ValueError as e:
    print('value must be interger', e)
except Exception as e:
    print(' error', e)

finally:
    print('connection closed')
