from enum import nonmember


class Student:
    def __init__(self):
        pass
    def sum(self, a=None, b=None, c=None):

        if a!=None and  b!=None and  c!=None:
            sum = a + b + c
        elif a!=None and b!=None:
            sum = a + b
        else:
            sum = a

        # return sum

        print(sum)


s=Student()
s.sum(1)




# result=s.sum(1, 2)
# print(result)