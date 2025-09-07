def my_decorator(func):
    def inner(a, b):
        if a<b:
            a,b=b,a
            return func(a,b)
        else:
            return func(a,b)
    return inner

def div(a, b):
    return a / b

div=my_decorator(div)
print(div(2,1))
