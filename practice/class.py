class Person:
    def __init__(self):
        self.age=30
        self.name="priyanka"
        self.lap=self.Laptop()


    def show(self):
        print(self.name, self.age)

    class Laptop:
        def __init__(self):
            self.brand= 'HP'
            self.model= '720'

        def show(self):
            print(self.brand, self.model)


p1=Person()
p1.show()

lap1=Person.Laptop()
lap1.show()


