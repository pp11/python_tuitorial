list=[1,5,6,2,10]

position=-1
def search(list, num):
    n=0
    for i in list:

        if i==num:
            n=n+1
            # print(n)
            globals()['position']=n
            return True
        else:
            n = n + 1


    return False

if search(list, 6) :
    print('found at position', position)
else:
    print('not found')

# search(list, 2)