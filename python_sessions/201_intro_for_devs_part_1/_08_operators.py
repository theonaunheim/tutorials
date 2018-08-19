'''
                              _
   ___  _ __   ___ _ __ __ _| |_ ___  _ __ ___
  / _ \| '_ \ / _ \ '__/ _` | __/ _ \| '__/ __|
 | (_) | |_) |  __/ | | (_| | || (_) | |  \__ \
  \___/| .__/ \___|_|  \__,_|\__\___/|_|  |___/
       |_|

'''
##============================================================================
## Operators
##============================================================================
##
## Where types can be thought of objects, operators can be thought of as the
## glue through which those objects interact with one another to describe
## more complex relationships
##
## Here are a list of operators:
##
## https://docs.python.org/3/reference/lexical_analysis.html#operators
##
## +       -       *       **      /       //      %      @
## <<      >>      &       |       ^       ~
## <       >       <=      >=      ==      !=
## or      any     all     and     not     is      in     for
##
## For evaluation order and operator precedence:
## https://docs.python.org/3/reference/expressions.html#evaluation-order
##
##============================================================================
## Boolean Operators
##============================================================================
##
## These booleans are associated with the operators 'and', 'or', 'any', 'not',
## and 'all'. Note: these work via short circuiting:

# and is True if are True, otherwise False.
True and True                   # True
False and False                 # False
True and False                  # False

# or is True if either are True, otherwise False
True or True                    # True
True or False                   # True
False or False                  # False

# any is True if any element is True, otherwise False
any([True, True, False])        # True
any([False, False])             # False

# all is True if all elements are True, otherwise False
all([True, True, True])         # True
all([False, True, True])        # False

# not is negation. not True is False. Not False is True.
not True                        # False
not False                       # True

##============================================================================
## Comparison Operators
##============================================================================

# Less than is True if the left item is less than the right.
5 < 10      # False
5 < 5       # False
5 < 1       # True

# Greater than than is True if the left item is greater than the right.
5 > 10      # False
5 > 5       # False
5 > 1       # True

# Less than or equal is True if the left is less than or equal to the right.
5 <= 10     # True
5 <= 5      # True
5 <= 1      # False

# Greater than or equal is True if the left is greater than or equal to right.
5 >= 10     # False
5 >= 5      # True
5 >= 1      # True

# Equal is True if the values are equal
5 == 5      # True
5 == 1      # False

# Not equal is True if the values are not equal
5 != 5      # False
5 != 1      # True

# is is object identity
True is True        # True
True is False       # False

# is not is negated object identity
True is not False   # True
True is not True    # False

##============================================================================
## Arithmetic Operators
##============================================================================
##
## Arithmetic operators are largely the same as you would see in any other
## language or math textbook.

# '+' gives the sum of two items.
5 + 10      # 15

# Note, '+' is also used for string concatenation.
'abcdefghijklm' + 'nopqrstuvwxyz' # the alphabet.

# '-' gives the difference between two items when used in a binary fashion.
5 - 10      # -5

# '*' gives the product of two items.
5 * 10      # 50

# '/' gives the quotient of two items
5 / 10      # .5

# '/' has also been repurposed for path creation.
import os
import pathlib
root = pathlib.Path('C:/')
this_folder = root / 'Users' / os.environ['USERNAME'] / 'Desktop'
/
# '//' floored or truncating division of two items.
7 // 3      # 2

# '%' modulo or remainder
7 % 3       # 1

# '-' also doubles as negation when unary.
-5          # -5

# abs() is the absolute value.
abs(-5)     # 5

# int() converts to int.
int('5')    # 5

# float() converts to float.
float(5)    # 5.0

# ** is exponent.
5 ** 2      # 25

##============================================================================
## In
##============================================================================

# In is used for inclusion, used with some sort of sequence type
'a' in 'aye'   # True

1 in [1, 2, 3] # True

##============================================================================
## Bitwise Operators
##============================================================================
##
## x | y        bitwise or of x and y
## x ^ y        bitwise exclusive or of x and y
## x & y        bitwise and of x and y
## x << n       x shifted left by n bits
## x >> n       x shifted right by n bits
## ~x           the bits of x inverted
##
##============================================================================
## Delimiters
##============================================================================
##
## We also have delimiters which serve a variety of purposes.
##
## (       )       [       ]       {       }
## ,       :       .       ;       @       =       ->
## +=      -=      *=      /=      //=     %=      @=
## &=      |=      ^=      >>=     <<=     **=

# Parenthesis are used for functions. Commas are used for separating
# arugments or items.
def add_items(item_1, item_2):
    return item_1 + item_2


# Parentheses are also used for tuples
my_tuple = (1, 2, False)

# Curly braces are for delimiting dicts or format sequences
my_dict = {1: 'one', 2: 'two'}

# Colons are used for lambdas
lambda x: x + 1

# ... and dictionaries
my_dict = {'key': 'value'}

# ... and slicing
my_list = list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
my_slice = my_list[2:]

# ... and compound statements when added at the end of a line.
class MyClass(object):
    pass


# Brackets are used for indexing, __getitem__() etc.
my_list = ['a', 'b', 'c']
my_dict = {'key': 'value'}
print(my_list[0])
print(my_dict['key'])

# See also += and -=
a = 1
a += 1
print(a)
a -= 1
print(a)

##============================================================================
## Overloading
##============================================================================
##
## See also: https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
##
## Quick note: operators overloading is accomplished via so-called 'magic'
## methods (not a name or designation I created. Seriously, that's what they
## are called). If we want to change how an object reacts to a plus sign, we
## would override our object's __add__() magic method like this:


class JankyInteger(object):
    '''This is a toy integer type that adds to 1 greater than it should.'''

    def __init__(self, wrapped_integer):
        self._integer = wrapped_integer

    def __add__(self, other):
        rv = self._integer + other + 1
        return rv

    def __radd__(self, other):
        rv = self._integer + other + 1
        return rv


jint_5 = JankyInteger(5)
jint_7 = JankyInteger(7)

print('10 + JankyInteger(5) is:')
print(10 + jint_5)
print()
print('JankyInteger(5) + JankyInteger(7) is:')
print(jint_5 + jint_7)

##============================================================================
# Questions
##============================================================================

