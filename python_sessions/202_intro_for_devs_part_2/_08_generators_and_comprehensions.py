r'''_07_generators_and_comprehension.py
                                 _                                   _ 
  __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ ___    __ _ _ __   __| |
 / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__/ __|  / _` | '_ \ / _` |
| (_| |  __/ | | |  __/ | | (_| | || (_) | |  \__ \ | (_| | | | | (_| |
 \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|  |___/  \__,_|_| |_|\__,_|
 |___/                                                                 
                                    _                    _             
  ___ ___  _ __ ___  _ __  _ __ ___| |__   ___ _ __  ___(_) ___  _ __  
 / __/ _ \| '_ ` _ \| '_ \| '__/ _ \ '_ \ / _ \ '_ \/ __| |/ _ \| '_ \ 
| (_| (_) | | | | | | |_) | | |  __/ | | |  __/ | | \__ \ | (_) | | | |
 \___\___/|_| |_| |_| .__/|_|  \___|_| |_|\___|_| |_|___/_|\___/|_| |_|
                    |_|                                                

'''
##=============================================================================
## Generally
##=============================================================================
##
## Python has good support for iterators and has stolen a lot of great ideas
## from other programming languages.
##
## For more detail, see:
## https://wiki.python.org/moin/Iterator
## https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
## https://wiki.python.org/moin/Generators
##
##=============================================================================
## Iterables
##=============================================================================
##
## Python provides basic support for iterables at a low level. Lists,
## tuples, dictionaries, files, and pretty much everything can be gone
## through element by element with the 'for item in iterable' syntax.
sample_list = [
    'Ever tried. Ever failed.',
    'No matter. Try again.',
    'Fail again. Fail better.',
]

# This is 'iterable', meaning it can be gone over one element at a time.
for phrase in sample_list:
    print(phrase)

# Fun fact, this roughly equivalent to:
try:
    # Iterable != iterator. Iterator is an object that serves as a proxy for
    # the iterable. You generally won't need to worry about that.
    iterator = iter(sample_list)
    while True:
        next_item = next(iterator)
        print(next_item)
except StopIteration:
    pass

## At the end of an iterator, the StopIteration is raised.
## You can make your own iterator classes using the __next__() method.
##
##=============================================================================
## List/Tuple/Dictionary comprehensions
##=============================================================================
##
## Many languages are functional constructs such as map(), filter(),
## reduce(), and anonymous lambda functions. Python is no different,
## but it also support for a more Pythonic solution called comprehensions.

# Say you have a list of temperatures in Fahrenheit that you want to convert
# to Centigrade:
f_temperatures = [31.5, 90.8, 34.6, 55.5, -10.5]

# We could easily write a function for converting these temperatures
# and then stick the output in a new list.
def convert(fahrenheit):
    centigrade = (fahrenheit - 32) * 5/9
    return centigrade


# Create list
c_temperatures = []

# Iterate through each temp
for f_temp in f_temperatures:
    # Convert temp
    c_temp = convert(f_temp)
    # Add temp to output list
    c_temperatures.append(c_temp)

# Print temps.
print(f_temperatures)
print(c_temperatures)

## Python has a better way to do this from a syntax perspective called
## the list comprehension. In a single statement, we can apply a function
## across a list and get the result with the following format:
##
## [ STATEMENT for ITEM in ITERABLE ]
## or
## [ STATEMENT if CONDITION else STATEMENT for ITEM in ITERABLE]
##
## This essentially creates a generator, and then expands it inside
## a list.

# So more succinctly we can do the above operation as:
c_temperatures = [convert(f_temp) for f_temp in f_temperatures]

# Or on multiple lines
c_temperatures = [
    convert(f_temp) 
    for f_temp 
    in f_temperatures
]

print(c_temperatures)

# These need not be defined functions.
c_temperatures_string = [
    'Below Freezing'
    if f_temp < 32
    else
    'Above Freezing'
    for f_temp
    in f_temperatures
]

print(c_temperatures)

# We can also use implicit lambdas.
k_temperatures = [c_temp + 273 for c_temp in c_temperatures]

# We can use zip and tuple unpacking if we want multiple values as a part.
print([
    '{c} Centigrade is {k} Kelvin.'.format(c=round(c_temp), k=round(k_temp))
    for c_temp, k_temp
    in zip(c_temperatures, k_temperatures)
])

# Finally, we can also do this with tuples and dictionaries.
k_temperatures = (c_temp + 273 for c_temp in c_temperatures)

# Dictionary comprehensions use the following format:
# {key: value for key, value in ITERABLE_YIELDING_TWO_ITEMS}
lower_dict = {
    'key_1': 'value_1',
    'key_2': 'value_2'
}

# To change to upper case.
upper_dict = {
    key.upper(): value.upper()
    for key, value
    in lower_dict.items()
}

print(upper_dict)

# These can also be nested if need be, but use caution. These get to be
# 'write only' very quickly.

nested = [(item_1, item_2) for item_1 in [1,2,3] for item_2 in [4,5,6]]
print(nested)

##=============================================================================
## Generators
##=============================================================================
##
## In addition, we can make iterable functions that have a memory of previous
## values. These are known as generators within Python.

def gen_func(start_number):
    while start_number < 10:
        start_number += 1
        yield start_number


gf = gen_func(5)

print(next(gf))
print(next(gf))

for result in gf:
    print(result)

# Generators also support sending values by putting yield on the
# right side of an assignment. Note, these types of generators
# must initially be send a value of None to start them.
def recv_gen_func(start_number):
    while start_number < 100:
        recv_value = (yield start_number)
        start_number += recv_value


# We instantiate our generator
rgf = recv_gen_func(20)

# next(generator) is essentially generator.send(None)
next(rgf)

# We send numbers in the list.
try:
    for number in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]:
        rv = rgf.send(number)
        print(rv)
except StopIteration:
    print('Done!')

##=============================================================================
# Questions?
##=============================================================================

