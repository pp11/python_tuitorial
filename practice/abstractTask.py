from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def process(self):
        print('it is abstract method')
        pass

class Laptop(A):
     def process(self):
         print('it is running')

class Programmer:
    def work(self, com):
        print('solving bugs')
        com.process()

class Whiteboard():
    def write(self, com):
        print('white')

# a=A()
# a.process()

lap=Laptop()
# lap.process()
whiteBoard=Whiteboard()
prog1=Programmer()
prog1.work(lap)

