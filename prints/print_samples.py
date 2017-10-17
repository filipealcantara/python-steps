# basic print string
print("myBeautifulString")

# passing an array
print(["m", "y", "A", "r", "r", "y"])

# splitting the array as positional arguments
print(*["m", "y", "A", "r", "r", "y"])

# printing the array as one string
print(*["m", "y", "A", "r", "r", "y"], sep="")

# printing two lines as one string
print(*["m", "y"], sep="", end="")
print(*["A", "r", "r", "y"], sep="")

# prints to a file
fsock = open("debbuging.log", "w") # this returns a file object that has a write(string) method
print("Printing in a file debbuging my code", file = fsock)

# outputs each print in execution time to the default output
print("MyFirstPrint", flush=True)
print("MySecondPrint", flush=True)
print("MyThirdPrint", flush=True)
