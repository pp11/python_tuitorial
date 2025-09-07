class A:
    def show(self):
        print('this is class A show')

class B(A):
    def show(self):
        print('this is class B show')


a=B()
a.show()