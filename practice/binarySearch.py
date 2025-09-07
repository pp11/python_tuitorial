

list=[3,5,6,7,8,11]
pos=-1
def search(list, num):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==num:
            globals()['pos']=mid

            return True
        else:
            if list[mid]<num:
                l=mid+1
            else:
                u=mid-1
    return False

if search(list, 5) :
    print('found at position', pos)
else:
    print('not found')
