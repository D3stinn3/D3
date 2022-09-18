import random
import itertools
import numpy as np
import datetime

def attempt(x):

    try:
        return float(x)
    except (TypeError, ValueError):
        print('this is not a float number')

attempt('sick')


def addition_for_loop():

    x = 15
    total = 0

    for number in range(x, x+1):

        total += number

    return total

print(addition_for_loop())

def break_statements():

    animals = ['dog', 'bat', 'fish']

    for name in animals:

        if name == 'fish':
            break

        print('Cool animal: ', name)
    
    print('These are amazing animals!')

break_statements()

def independent_infinite_loop():

    number = int(input('Enter number to be assessed: '))
    counter = 1
    total = 0

    while counter <= number:

        total += counter
        counter += 1

    return total, counter

print(independent_infinite_loop())

def break_as_else():

    letters = 'aeiou'

    while True:

        letter = input('Enter a letter: ')

        if letter in letters:
            break # assists in breaking out of the loop!

        print('letter not in letters, please try again') # here break acts as an else statement in the infinite loop

    print('perfect, letter in letters!')

break_as_else()

def break_as_break():

    while True:

        input('press enter to draw a number')

        number = random.randint(1, 10)

        print('You got ', number)

        choice = input('do you wish to continue? (y/n): ')

        if choice == 'y':
            continue

        elif choice == 'n':

            print('operation ended...')
            break

break_as_break()

def operations(object_one):

    if iter(object_one) is True:

        print(f'{object_one} is iterable')
    
    else:

        print(f'{object_one} is not iterable')

operations([1, 2, 3])

def gen():

    for i in range(1, 10):
        yield i ** 2


def special_gens():

    family_names = ['Albert', 'Anisia', 'Amy', 'Destinne', 'Argwins']

    first_letter = lambda x: x[0]

    for letter, grouping in itertools.groupby(first_letter, family_names):

        pass


"""numpy for data science"""
"""NUMPY deals with arrays and is much faster operational than python iterables!"""

def arrays_vs_python_iter():

    my_array = np.arange(100) # np is a way to handle iterables much faster than the python objects
    my_list = list(range(100))

    data = np.random.randn(2, 2)

    print(data)

    arr = np.array(my_list)
    arr2 = np.array(my_array)

    dimension1, dimension2 = arr.ndim, arr.ndim

    print(dimension1, dimension2)

    print(arr)
    print(arr2)

arrays_vs_python_iter()
