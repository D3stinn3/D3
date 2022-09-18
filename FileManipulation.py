print("Hello World!")

"""file operatons"""

# there are four basic python file operations
# open, read, write, close

"""the open(), write() and close() func"""
# facilitates the opening of a file for reading, writing or both as well as appending!
# this is the format/syntax for the open func in python file_object=open(filename [, access_mode][, buffering])
# the file_object is considered to be the handle, followed by the open func and the name of the file alonside various methods
# The access mode is an optional parameter that allows you to indicate the mode in which you wish to access the file
# Options include read, write, or append
# file can be opened in either binary or text mode where one works with strings and the other, well, binary!

f = open("newfile.txt", "w")

# the f object returns "<_io.TextIOWrapper name='newfile.txt' mode='w' encoding='UTF-8'>
# to write to a file --->

num_of_char = f.write("Destinne First File!")
print(int(num_of_char)) # this prints out the number of chars in the "newfile.txt"

# close your files properly to free up the resources used and to avoid accidental deletion or modification

f.close()

"""the readlines() method!"""
# in order to read a file, the file must be open in read mode!
f1 = open("newfil.txt", "w")
num_of_char2 = f1.write("Destinne File Management System Tutorial!")
print(int(num_of_char2))

f1.close()
f2 = open("newfil.txt", "r")
# easy way to read and parse each line in a text file
mistari = f2.readlines()
print(mistari)

"""list comprehensions in course"""

# the read file generates a list, this is a chance to practice list comprehensions!
# (values) = [(expression) for (value) in (collection)]
 
mistari_halisi = [x for x in mistari if x == "Destinne File Management System Tutorial!"]
mistari_isio_halisi = [x for x in mistari if x == None]

# the list comprehension checker...
print(mistari_halisi)
Checker = bool(mistari_halisi)
Checker1 = bool(mistari_isio_halisi)
print(Checker)
print(Checker1)

def deconstruction(Checker=Checker):

    while mistari_halisi:

        for x in mistari:
            print(mistari)
            break
        
        break

    return Checker

print(deconstruction())

f2.close()

# For Text modes you have "r", "w", "a"
# For Binary modes you have "rb", "wb", "ab"
# if file dont exist in "w", and "a", python creates the file itself



"""python decorators"""

# also touching on python decorators in the course
# python decorators allows you to change the behavior of a functions without changing the file iteself
# this is also known as metaprogramming because a part of the program tries to modify another part of the program at compile time

"""how to create a basic python decorator"""

# decorators, functions are taken as the argument into another function

def decorator_yangu(func):

    def wrapper_func():

        # this is where you do something before the function

        func()

        # this is where you do something after the function

    return wrapper_func

"""to use the predetermined decorator..."""

@decorator_yangu
def my_func():

    pass

"""perfect example"""

# decorator fuction

def i_am_the_decorator(func):

    def i_am_being_decorated(): # defines the argument!
        print("Nimedecoratiwa")
        func()
    return i_am_being_decorated

# to decorate an ordinary func

@i_am_the_decorator # python begins by executing the decorator
def ordinary(): # then executes the function
    print("Mimi ni ordinary Func!")

ordinary()


"""decorators for smart functions"""

# lets define a normal divide function!

def divide(a, b):

    return a/b

# traditionally one has to call the function to define the arguments...
smart_func = divide(4, 2)
print(smart_func)

# however, the the issue can be handled by decorators intrinsically

def smart_divide(func):

    def inner(a, b):

        if b <= 0:
            print("Error! cannot divide!")

        return func(a, b)

    return inner


@smart_divide
def gawanya(a, b):

    return a/b

smart_division = gawanya(2, -1) # notice that we call the gawanya function without invoking the smart divide
print(smart_division) # this is a cool feature that provides a platform where two functions can interact without changing the host func!

# this is the technology used by frameworks such as flask and modules such as discord.py to interact with the scripts without changing them

def smart_door(func):

    # The code is a valve
    def unlock(open, close):

        if open == "opened":
            print("Open valve is closed!")
            return
        
        elif close == "closed":
            print("Closed valve remains closed")
            return

        return func(open, close)
    return unlock

@smart_door
def control(open, close):

    presence = True

    if presence is True:
        return open
    else:
        return close

smart_control = control("opened", "closed")
print(smart_control)
















