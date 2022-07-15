import random
import operator


class devops:

    def __init__(self, cashin, cashout, totalpay):
        self.cashin = cashin
        self.cashout = cashout
        self.totalpay = totalpay

    def cashflow(self):
        if self.cashin > 100 in range(1, 1000):
            print('good price')
        elif self.cashin < 100 in range(1, 1000):
            print('not good pricing')
        if self.cashout > 50 in range(1, 1000):
            print('brilliant cashout')
        elif self.cashout < 50 in range(1, 1000):
            print('cashout is too much')
        return self.cashin + self.cashout


reg = devops(85, 57, 100)
print(reg.cashflow())


def learning_lists():
    print("lists can be change or manipulated in place, this is true because the list type is mutable!")
    list1 = ['Destinne', 'Maria', 'Caleb', 1]
    list2 = ['Gash', 'lempa', 'maureen']
    for i in list1:
        print("Here is a practical way to show this fact!")
        # the statement above loops over the number of iterables in the list!
        if i == 1:
            list1[-1] = 'Amy'
        elif i == 'Destinne':
            list1[0] = 'D3stinn3'
    list1.append('justo')
    list1.append(list2)
    try:
        print('{0} this is the list and might not have an attribute!'.format(list1))
        '.'.join(list1)

    except TypeError:
        print('Hio object list haina hio attribute!')
    print(f"Here is the new list formed: {list1}")


learning_lists()


def interview_schedule():
    print("Compounding Intervals")
    print("[H] Hourly")
    print("[D] Daily")
    print("[W] Weekly")
    print("[M] Monthly")
    print("[Y] Yearly")


def interest_rate():
    hour = 1 / 24
    day = 1
    week = 7
    month = 30
    year = 365
    principal = float(input("Starting balance (in $): "))
    comp_interv = input("Enter compounding intervals: ")
    print("Compounding frequency")
    interview_schedule()  # indicates function call in order to get parse compounding intervals

    if comp_interv == "H":
        comp_fn = hour
        hour = input("Compound every X Hours: ")
        print(comp_fn, " going for ", hour)

    elif comp_interv == "D":
        comp_fn = day
        day = input("Compound every X Days: ")
        print(comp_fn, "going for", day)

    elif comp_interv == "W":
        comp_fn = week
        week = input("Compound every X Weeks: ")
        print(comp_fn, week)

    elif comp_interv == "M":
        comp_fn = month
        month = input("Compound every X Months: ")
        print(comp_fn, "going for", month)

    elif comp_interv == "Y":
        comp_fn = year
        year = input("Compound every X Years: ")
        print(comp_fn, " going for ", year)
    apr = float(input("Enter annual interest rate (%): "))
    final = principal * (1 + (apr / 100) / 365) ** 365
    print(final)


def kenyans_on_discord():
    print('Announcements made on kenyans on discord server are passed here!')
    k_o_d = ['D3stinn3', 'Kiama_muu', 'others']

    if k_o_d[1] == 'Kiama_muu':
        k_o_d.append('lost people')
        k_o_d.insert(2, 'Maria')
        print('Hello this is kiama')
        print(k_o_d)
    first_dict = {x: x.lower() for x in k_o_d}
    print(first_dict)
    print(first_dict.get('Maria'))


kenyans_on_discord()


def fun_with_lists():
    for x in range(1, 2, 3):
        print(x)
    lissst = ['hello', 'destinne']
    for x in 'destinne':
        print('this is the creation process of the list in {}!'.format(x))
        lissst.append([x + f'{x}'])
        print(lissst
              )
        # append and extend methods grow a list in-place
        # methods sort,replace: order and reverse lists, the insert method inserts an item at an offset
        # methods remove,pop: delete from a list by value and by position, the del statement deletes an item or slice
    list0 = [f for f in lissst]
    print(list(list0))
    list01 = [0]
    list012 = [x ** 5 for x in list01]
    print(list012)
    list1 = ['abc', 'ABD', 'aBe']
    list1.sort(key=str.lower, reverse=True)
    print(list1)
    list2 = ['aB', 'Bc', 'aa']
    sorted(list2, key=str.upper, reverse=True)
    print(list2)
    list2.reverse()  # reverses the list sequence
    del list2[0]
    print(list2)
    list3 = ['TRINITY', 'MARIA', 'DESTINNE']
    sorted([x.lower() for x in list3], reverse=True)
    list3.extend(['AMY', 'ARGWINS'])
    for i in list3 and list2:
        print(f'{i} is here')  # prints out the first list
        list(reversed(list3))
    list4 = ['makini', 'risingstar', 'lambaglory']
    list4.insert(2, 'soweto')
    sorted(list4, key=str.upper, reverse=True)
    list4.pop(3)
    print(list4)
    print(list3)


fun_with_lists()


def fun_with_dictionaries():
    d1 = {'name': 'Destinne', 'age': 21, 'height': 6}  # Conventional literal expression for any dictionary creation
    d1k = d1.keys()
    print(d1k)
    d2 = dict(name='Anyssya', age=55, height=7)  # dict keyword argument form, but it requires all keys to be strings
    d2k = d2.keys()
    print(d2k)
    d4 = dict.fromkeys('name', 'age')  # the from-keys function here deconstructs of the first key by index and a value
    d5 = dict.fromkeys(['name', 'age'])  # the from-keys function here registers a NoneType in dict key/value tuples
    # form
    d9 = dict([('key', 'value'), ('key1', 'value1')])  # build up keys and values as sequences at runtime
    print(d9)
    d1k1 = d1['name'][0:]  # string indices must be integers to implement fast key lookup (a.k.a. hashing)
    d1k2 = d1['age']
    d1v1 = d1.values()  # returns the values for the dictionary d1
    d1i1 = list(d1.items())
    d1g1 = d1.get('Residence', 'Nairobi')  # the get method returns a value None assigned a value Nairobi
    G = {}
    G[(2, 3, 4, 5)] = 10  # Assign by keys dynamically for any dictionary creation one field at a time
    G[(5, 4, 3, 2)] = 20
    G[(6, 7, 8, 9)] = 0
    G[(9, 8, 7, 6)] = 5
    G[('beth', 'maria', 'caleb')] = 15
    G[('unga mix', 'mchele', 'chapati')] = 'omena'
    print(G.update(d1))
    A = dict(zip(['a', 'b', 'c'], [1, 2, 3]))  # Make a dict from zip result
    B = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
    C = {i: t for (i, t) in zip(['SKUMA', 'WARU', 'BEANS'], ['UGALI', 'CHAPATI', 'BHAJIA'])}  # dict comprehensions
    D = {x: x ** 2 for x in [2, 3]}
    print(D)
    print(A, B, C, G)
    get_method = d1.get(('name', 'Destinne'), 0)
    listt = ['Alex', 'Doom', 'Inactive']
    E = {n.upper(): n.lower() for n in listt}  # Loop over any iterable! to turn list into dict while modifying
    F = {n.lower(): 0 for n in listt}
    H = dict.fromkeys(['alex', 'doom'], 0)
    print(H)
    print(F)
    print(E)
    print(get_method)
    print(list[G.items()])
    print(d1k1, d1k2, d1v1, d1i1, d1g1)
    print(d4, d5)
    for d1['name'] in d1:
        print(f'hello its Destinne in {d1}')  # parses the name iterable from the dict d1
        d1['height'] = 7
        print(f'hello its Destinne"s height in {d1}')  # changes key value to 7 from the initial height 6
    d6 = d1.update(d2)
    print(f'the updated Destinne"s list be like: {d6}')  # returns a NoneType value!
    print(list(d1.keys() and d2.keys()))
    try:
        d3 = (d2, d1)  # this is a nested list but is possible using the () call not the {} call
        print(d3)
        print('nesting un-hashable type is very possible')
        print(G['beth', 'maria', 'caleb'])
    except TypeError or KeyError:
        print('this always contributes to a type error!')
        print(f'{G} produces key error!')

    table = {"python": "Guido Van Rossum",
             "Tcl": "John Ouhster",
             "Perl": "Larry Wall"}
    language = 'Tcl'
    creator = table[language]
    print('Introducing mr.poor programmer! ' + creator + "!")
    print(f'{creator} is our winner for the moment! ')
    for lang in table:  # Same as: for lang in table.keys() this is also a for loop thwarted by the return call
        #  simply iterates through each key in the table and prints a tab-separated list of keys and their values
        print('in the cast with ...' + '\t' + lang, '\t', table[lang])
        if lang == 'python' or lang == 'Tcl' and lang == 'Perl':
            print('Guido was chosen! for the next moment!')
            return creator
    print(f"{language} was the fighting ground")


def list_and_dict():
    table1 = {(1, 2, 3): 'trilogy',
              (3, 2, 1): 'reverse_trilogy'}  # the dictionary is paramount when dealing with heavy information or data
    number_reps = (1, 2, 3)
    actual_number = table1[number_reps]
    print('representatives of ' + actual_number)
    while True:
        if table1[(1, 2, 3)] == 'trilogy':
            print('this is my first dictionary test!')
            for testing in range(1, 5):
                print('this while loop works perfectly')
                break  # the break statement stops or a breakpoint for this while loop
        if table1[(3, 2, 1)] != 'reverse':
            try:
                print('this is my second dictionary test!')
            except TypeError:
                print('a type error exists here!')
            for testing1 in range(1, 5):
                print('this while loop also works perfectly!')
                break
        break
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'diamonds', 'spades', 'hearts', 'flowers']
    symbol = ['kings', 'queens', 'ace', 'joker']
    card_and_symbol_shuffle = {x: x.upper() for x in random.choice(cards and symbol)}
    card_and_symbol_shuffle1 = {x: k for (x, k) in zip(cards, symbol)}  # this becomes the implicit shuffle
    print(card_and_symbol_shuffle, card_and_symbol_shuffle1)

    print('Enter a symbol name: ')
    name = input()
    if name not in symbol:
        print('sina card symbol by the code %s' % name)
    else:
        print('%s is in my cards symbol list' % name)  # in and not in statements translates to true or false...

    cat = ['fat', 'white', 'lazy']
    size, color, disposition = cat  # this is the value unpacking method a.k.a. multiple assignments trick

    print(f'start ({len(cat)}')
    badwords = []
    for word in cat:
        if len(set(list(word))) != len(list(word)):
            badwords.append(word)
    for dword in badwords:
        cat.remove(dword)
    print(f'first filter, no dupe letters {len(cat)}')

    for i in symbol:
        print('the for loop iterates over the length of the list in question')
        print(f'{i} is an item in the symbol list ' + symbol[3] + ' as ' + str(i))  # symbol is a global variable!
        total_number_of_iterations = len(cards)
        print(total_number_of_iterations)
        # Dictionaries are mappings, not sequences
    D = {99: 'spam'}
    if D[99] != 'spam':
        print(f'{D}')

    while True:
        card = random.choice(cards)
        symbols = random.choice(symbol)  # this become the explicit shuffle!
        if str(card) + 'of' + str(symbols) == '2 of kings':
            print('trying out this guess')
        elif str(card) + 'of' + str(symbols) == 'diamonds of joker':
            print('this guess is so random')
        elif str(card) + 'of' + str(symbols) == '6 of queens':
            print('yet another random guess!')
        break


fun_with_dictionaries()
list_and_dict()


def dict_formation():
    first_dict = {'name': 'Destinne', 'age': 25}
    second_dict = dict(name='Destinne', age=25)
    third_dict = dict.fromkeys(['name', 'age'])
    forth_dict = {x: y for (x, y) in zip(['name', 'age'], ['Destinne', 25])}

    while True:
        if first_dict.keys() != third_dict.items():
            print('they are the same...')
        else:
            print('they are not the same...')
        if  first_dict.values() != forth_dict.values():
            print('they are also the same!')
        else:
            print('they are also not the same!')
        break
    second_dict['age'] = 26
    forth_dict['name'] = 'Wajackoyah'
    print(second_dict)
    print(forth_dict)

dict_formation()

def dict_in_calc():
    action = {
        '+': operator.add,
        '-': operator.sub,
        '/': operator.truediv,
        '**': operator.pow
        }

    print(action['**'](6, 2))

dict_in_calc()