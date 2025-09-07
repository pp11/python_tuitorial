class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        s1=self.m1+other.m1
        s2=self.m2+other.m2
        s3=Student(s1,s2)
        return s3

    def __gt__(self, other):
        s1=self.m1+other.m1
        s2=self.m2+other.m2

        if s1>s2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1,  self.m2)

s1=Student(50,78)
s2=Student(65,67)



n=s1+s2
print(n.m1,n.m2)

if s1>s2:
    print('s1 wins')
else:
    print('s2 wins')



print(s1)