class A:
    def __init__(self):
         print("A init")

    def feature1(self):
        print('this is A feature1')
    def feature2(self):
        print('this is feature2')

class B():
    def __init__(self):
        super().__init__()
        print("B init")


    def feature1(self):
        print('this is  B feature1')
    def feature4(self):
        print('this is feature4')

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C init")
    def feature5(self):
        print('this is feature5')
    def feature6(self):
        print('this is feature6')



b=C()
b.feature1()


# class A:
#     def feature1(self):
#         print('this is feature1')
#     def feature2(self):
#         print('this is feature2')
#
# class B():
#     def feature3(self):
#         print('this is feature3')
#     def feature4(self):
#         print('this is feature4')
#
# class C(A,B):
#     def feature5(self):
#         print('this is feature5')
#     def feature6(self):
#         print('this is feature6')
#
#
# a=A()
#
# b=B()
# c=C()
#
