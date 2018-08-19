'''
                  _        _
   ___ ___  _ __ | |_ __ _(_)_ __   ___ _ __ ___
  / __/ _ \| '_ \| __/ _` | | '_ \ / _ \ '__/ __|
 | (_| (_) | | | | || (_| | | | | |  __/ |  \__ \
  \___\___/|_| |_|\__\__,_|_|_| |_|\___|_|  |___/

'''
##=============================================================================
## Generally
##=============================================================================
##
## Containers will make your life much easier. Probably one of the best "bang
## for your buck" things you can teach yourself is the attributes and methods
## of the standard library containers and how to use them.
##
## See also: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
## See also: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
## See also: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
##
##=============================================================================
## List
##=============================================================================
##
## Python lists are not your grandfather's arrays. They are automatically
## expanding, mutable types that can hold heterogeneous items. They are created
## with brackets of multiple items separated by commas.
##
## See also: https://docs.python.org/3.6/tutorial/introduction.html#lists
## See also https://docs.python.org/3.6/library/stdtypes.html#list

# Create heterogenous lists
list_1 = [50, None, 90, 900, 100]
list_2 = ['Word', True, list_1]

# Most importantly, lists can be iterated over:
for item in list_1:
    print(item)

## Lists can be indexed using bracket notation (note zero-based index). This
## is used to pick out individual elements from the list. Positive numbers
## start from the begining of the list, and negative numbers start from the
## end.
first_element = list_1[0]
second_element = list_1[1]
last_element = list_1[-1]
print(first_element, second_element, last_element)

# Lists can also be sliced, which returns a new list.
middle = list_1[1:3]
head = list_1[:2]
tail = list_1[1:]
print(middle, head, tail)

# We can concatenate lists
new_list = list_1 + list_2
print(new_list)

## And lists have the following methods (among others):
##
##   append:   add element to list without flatening.
##   count:    get the number of a certain element in a list.
##   extend:   add element to list with flatening.
##   index:    get index of certain item.
##   insert:   insert item at particular location.
##   pop:      remove last item.
##   remove:   remove an item from the list.
##   reverse:  reverse the order of a list.
##   sort:     sort the values based on a key.

list_3 = 'When I was a lad I served a term ...'.split()
print(list_3)

# append()
list_3.append('new')
print(list_3)

# extend()
list_3.append(['additional', 'items'])
list_3.extend(['additional', 'items'])
print(list_3)

# reverse()
list_3.reverse()
print(list_3)

# sort() you can supply custom keys
list_3.sort()
print(list_3)

# index()
print(list_3.index('lad'))

# insert() and remove()
list_3.insert(0, 'begin')
list_3.remove('lad')
print(list_3)

# pop()
item = list_3.pop()
print(item)
print(list_3)

# WARNING: some list methods don't return anything.
list_3 = list_3.append('a')
# This will likely yield unintended results.
print(type(list_3))

##=============================================================================
## Tuple
##=============================================================================
##
## Tuple are immutable types that are primarily used for storage. They are
## a convenient mechanism to provide an immutable return value from a function.
## They are created with parentheses and commas.
##
## See also: https://docs.python.org/3.6/library/stdtypes.html#tuple


def returns_tuple():
    return_val = ('First', 2, False)
    return return_val


# Get 3 return values from function.
my_tuple = returns_tuple()

# Like lists, tuples are iterable.
for item in my_tuple:
    print(item)

# The tuple unpacking is useful.
first, second, third = returns_tuple()
print(first)

## Use of the underscore when unpacking tuples throws away the value
## In the below case, only the third value in the tuple returned by the function
## is assigned a name
_, _, third = returns_tuple()


# Tuple functions are limited, but count()
count_2 = my_tuple.count(2)
print(count_2)

# and index() are useful.
index_2 = my_tuple.index(2)
print(index_2)

# Since parentheses are delimiters as well, single-element tuples need a comma.
i_am_a_tuple = (1,)
i_am_an_integer = (1)

##=============================================================================
## Dictionary
##=============================================================================
##
## Dictionaries are the unsung hero of the Python standard library. Use
## dictionaries. A lot. Your code will thank you later. Dictionaries are
## created with curly braces, colons, and commas. like this:
my_dict = {
    'Arthur':       'King of the Britons',
    'Sir Bedevere': 'the Wise',
    'Sir Lancelot': 'the Brave',
    'Sir Galahad':  'the Pure',
    'Sir Robin':    'the Not-Quite-So-Brave-as-Sir-Lancelot'
}

# We can access our elements using the following syntax.
val = my_dict['Arthur']
print(val)

# We can add items using the following syntax. They can hold whatever objects.
# This includes functions, modules ... whatever.
my_dict['key_3'] = bytearray([0, 127, 255])
print(my_dict)

# Keys need not be strings, but they do need to be hashable.
my_dict[4] = 'value_4'
print(my_dict)

# Keys can be deleted with the following syntax (one of the few uses of del)
del my_dict['key_3']

## If you want keys to be automatically created upon accessing, you can
## modify the dicts' default or simply use DefaultDict in the collections
## module.
##
## Dictionaries have a bunch of useful methods:
##
##   items       get all (key, value) tuples as an iterator.
##   keys        get all keys
##   setdefault  add a default key.
##   update      add another dict's keys to this dict
##   values:     get all values

# The most useful method is items().
for key, value in my_dict.items():
    print(str(key) + ' goes along with ' + str(value))

# keys()
print(my_dict.keys())

# values()
print(my_dict.values())

# setdefault()
my_dict['nonexistant key']
my_dict.setdefault(None)
print(my_dict['nonexistent_key'])
print(my_dict)

# update()
my_dict.update({'new_key_1': 'new_value_1', 'new_key_2': 'new_value_2'})
print(my_dict)

## Like lists, most of these methods don't return anything.
##
##=============================================================================
## Set
##=============================================================================
##
## Sets are used for set-theory like operations. They are also used for
## reducing a list to a set of unique values. They are created using curly
## braces, but without colons as seen with dictionaries.
##
## See also: https://en.wikipedia.org/wiki/Set_theory
## See also: https://docs.python.org/3/tutorial/datastructures.html#sets

# Example sets
set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

## Some of their useful methods are:
##   add:                    add an element to a set
##   difference:             get elements in one set and not another
##   discard:                get rid of item in set
##   intersection:           get items in both sets
##   symmetric_difference:   gets elements in one set but not other.
##   union:                  gets all values in both sets
##   update:                 add on set to another.

# add
set_1.add(1000)
print(set_1)

# difference
diff_1 = set_1.difference(set_2)
print(diff_1)
diff_2 = set_2.difference(set_1)
print(diff_2)

# discard
set_1.discart(1000)
print(set_1)

# intersection
intersect = set_1.intersection(set_2)
print(intersect)

# symmetric_difference
sym_diff = set_1.symmetric_difference(set_2)
print(sym_diff)

# union
union = set_1.union(set_2)
print(union)

# update
set_3 = {1000000, 10000000}
set_2.update(set_3)
print(set_2)

##=============================================================================
## Other
##=============================================================================
##
## What we've seen above are only the built in types. There is an entire
## 'collections' module with Counters, Dequeues, Default Dicts, and pretty
## much anything worth creating and/or using.
##
##=============================================================================
# Questions?
##=============================================================================
