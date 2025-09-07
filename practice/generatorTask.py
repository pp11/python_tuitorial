def topTen():
    #
    # yield 5
    # yield 6
    # yield 7
    i=1
    while i<=10:
        sq=i*i
        yield sq
        i=i+1


value=topTen()

for i in value:
    print(i)