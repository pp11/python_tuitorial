class Pycharm:
    def execute(self):
        print('compile')
        print('execute')

class Eclipse():
    def execute(self):
        print('spelling check')
        print('Eclipse')
        print('compile')
        print('execute')


class Laptop:
    def code(self, ide):
        ide.execute()

p=Pycharm()

e=Eclipse()

lap=Laptop()
lap.code(e)