def myFunction(*positional, **keywords):
    print(type(positional))
    print(positional)
    print(type(keywords))
    print(keywords)

myFunction(1, 2, 3, 4, a=5, b=6, c=7)