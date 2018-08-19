'''
 __        ___           _                      _   _          
 \ \      / / |__   __ _| |_    __ _ _ __ ___  | |_| |__   ___ 
  \ \ /\ / /| '_ \ / _` | __|  / _` | '__/ _ \ | __| '_ \ / _ \
   \ V  V / | | | | (_| | |_  | (_| | | |  __/ | |_| | | |  __/
    \_/\_/  |_| |_|\__,_|\__|  \__,_|_|  \___|  \__|_| |_|\___|
                                                            
  _               _         ___ 
 | |__   __ _ ___(_) ___ __|__ \
 | '_ \ / _` / __| |/ __/ __|/ /
 | |_) | (_| \__ \ | (__\__ \_| 
 |_.__/ \__,_|___/_|\___|___(_) 


'''
## ============================================================================
## So. Umm. Yeah.
## ============================================================================
##
## If you're anything like I was when I was first getting start, you're
## probably thinking, "At this point, I don't even know how much I don't know".
## That's totally normal! This section is to help give a little shape and
## definition to an otherwise nebulous topic.
##
## You may need some time to fully get your head around this, so don't worry if
## you don't completely understand it the first time around.
##
## See also:
##     https://docs.python.org/3/tutorial/introduction.html
##
##
## See also:
##     https://docs.python.org/3/tutorial/controlflow.html
##
## ============================================================================
## Whitespace
## ============================================================================
##
## I'm going to stop and discuss whitespace really quickly, because it will
## save you time in the long run if you go through the trouble to learn about
## it up front. Whitespace characters are things like spaces and tabs and
## newlines (e.g. the character inserted when you press return.
##
## Note: NEVER USE TABS INSTEAD OF SPACES.
##
## A lot of other languages use curly braces "{" and "}" to group statements
## togehter. Whitespace is used in Python to do the same thing. Let's do a
## hypothetical scenario where we perform certain actions if a number is less
## than 10 and other actions where a number is less than 5.

# We are assigning the integer 7 to the name 'number' 
number = 7

# We test if 'number' is less than 10. If it is less than 10, we run the
# block of indendted text. If not, we skip the entire block of indented text. 
if number < 10:
    # This only gets executed if the number is less than 10
    print('Starting less than ten commands.')
    # Same.
    print('Your number is less than 10!')

# We are now out of the previous block. If the number is less than 5, we run
# this block. If not, we skip.
if number < 5:
    print('Starting less than five commands.')
    print('Your number is less than 5!')

## In the case above with the number seven, this would print:
##
##     Starting less than ten commands.
##     Your number is less than 10.
##
## It would completely skip the less than 5 block. Feel free to tweek the
## numbers above and rerun the code.
##
## Whenever you see a line ending in a colon (":") you are basically telling
## Python, "Hey, Python! This is a compound statement! All the indented stuff
## following is associated with this statement!"
##
## This can go for functions, where the function body is indented:

def function_1():
    print('First line of function')
    print('Now returning')
    return True

## Or for conditionals:

if 5 > 2:
    x = 30
    y = 50

## Or classes or any other number of compound statements. Note: Python will get
## ornery if you indent stuff without a reason to do so.
##
## ============================================================================
## Variables / Names
## ============================================================================
##
## If you ever want to store stuff, you use a "name" (which we will also call a
## "variable" even though that's not technically accurate). You use the equals
## sign ("=") as an assignment operator to assign a value. Unlike most
## languages, you can put whatever you want in a name. Python don't curr.
##
## It will let you do whatever you want until you do something that makes no
## sense like this:
##
##     'rutabaga' / 5

# integer
x = 5

# strings are denoted with a single or double quote
x = 'disco'
x = 'rutabaga'

# list
x = list()

# Boolean
x = True

# Nonetype
x = None

## Note: you use '==' to compare items, not '='. You will make this mistake a
## billion and a half times.

# This will give you a syntax error if uncommented.
# 1 + 1 = 2

# This will yield True
1 + 1 == 2

## ============================================================================
## Functions
## ============================================================================
##
## See also:
##     https://docs.python.org/3/tutorial/controlflow.html#defining-functions
##
## See also:
##     https://en.wikipedia.org/wiki/Subroutine
##
## See also:
##     https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
##
## Functions are one of the key building blocks of modern computer programs.
## They will make your code clearer by bundling frequently executable code
## into blocks. Functions:
##
##    1) start with the 'def' keyword;
##    2) take zero or more arguments within a set of parentheses, and;
##    3) optionally can return a value to the caller.
##
## The functions can then be "called" using function() syntax
##
## We could write the following code:

print('Max, you are very, very, very cordially invited to join us.')
print('Leo, you are very, very, very cordially invited to join us.')
print('Ulla, you are very, very, very cordially invited to join us.')
print('Franz, you are very, very, very cordially invited to join us.')
print('Roger, you are very, very, very cordially invited to join us.')
print('Carmen, you are very, very, very cordially invited to join us.')
print('Mr. Marks, you are very, very, very cordially invited to join us.')

## Or you could write this as a function:

def get_greeting(input_name):
    output_greeting = input_name + ', you are very, very, very cordially invited to join us.'
    return output_greeting

print(get_greeting('Max'))
print(get_greeting('Leo'))
print(get_greeting('Ulla'))
print(get_greeting('Franz'))
print(get_greeting('Roger'))
print(get_greeting('Carmen'))
print(get_greeting('Mr. Marks'))

# Or alternatively you can use a for loop:

for name in ['Max', 'Leo', 'Ulla', 'Franz', 'Roger', 'Carmen', 'Mr. Marks']:
    print(get_greeting(name))

## Which is more maintainable and saves a bunch of typing.
##
## As you can seek, functions start with a "def" keyword followed by the
## function name (in this case, "get_greeting"). This is follwed with set of
## parenthesis which takes the function parameters (here, "input_name").
## Following that, a colon (":") indicates that the function has started and an
## indented block which shows the function. Inside this function, we put two
## strings together, and then return a value (in this case, "output_greeting").
##
## Later on, for each name we "call" this get_greeting function with an
## argument, like this:
##
##     get_greeting('Max')
##
## Which basically passes the string 'Max' into the function and then processes
## the string to make a new string 'Max, you are ...', and then passes the
## return value of the function back out of the function. The result of the
## get_greeting function was then printed. In other words:

print(get_greeting('Max))

## ... is equivalent to:

temporary_variable = get_greeting('Max')
print(temporary_variable)

# Note: print() is a function too.

## ============================================================================
## Flow Control
## ============================================================================
##
## Like any other language worth it's salt, Python has flow control. This can
## be used to do conditionals:

name = 'Glinda'

if 'linda' in name:
    print('Name contains linda!')
elif 'LINDA' in name:
    print('Name contains LINDA!')
else:
    print('Name does not contain linda or LINDA.')

## Or loops:

for name in ['Elphaba', 'Nessarose', 'Boq']:
    print(name)

x = 5

while x > 3:
    x = x - 1

## Or error handling. If you do something wrong, Python will tell you why.

try:
    print("Who is the man who would risk his neck for his brother man?")
    answer = shaft
except NameError:
    print("Can you dig it?")

## ============================================================================
## Objects, Attributes, and Methods
## ============================================================================
##
## Object-oriented programming is a deep topic that we can't cover here:
##     https://en.wikipedia.org/wiki/Object-oriented_programming
##
## One quick aside: everything in Python is an object. You can access an
## object's attributes (data about the object) and methods (actions that the
## object can do) using 'dot' notation. The attributes and methods will be
## different for each object type.
##
## Below, we tweak some string objects.

# Create a string
string = 'I am a regular string'

# Use the string's upper() method to capitalize it.
upper_case_string = string.upper()
print(upper_case_string)

# Use .__class__ attribute to get the class information of the object.
print('String is of the class:')
print(string.__class__)

# You can get a list of all objects and methods with dir().
print(dir(string))

## ============================================================================
## Containers
## ============================================================================
##
## See also:
##     https://docs.python.org/3/tutorial/datastructures.html
##
## Python has a bunch of containers that will make things easier for you, like
## lists:

sade_songs = ['Smooth Operator', 'King of Sorrow', 'Haunt Me']
sade_songs.append('Is it a Crime?')
sade_songs.sort()

# Prints 'Haunt ...', 'Is ...', 'King ...', 'Smooth ...' 
for song in sade_songs:
    print(song.upper())

# Use the [] notation for indexing. Note: Python indexing starts at 0.
print(sade_songs[0])

## ... and dictionaries:

captains = {
    'Deep Space 9': 'Benjamin Sisko',
    'Voyager'     : 'Kathryn Janeway',
    'Enterprise'  : 'Jean-Luc Picard a.k.a. The G.O.A.T.',
    'Filler'      : 'John Archer',
    'Also Filler' : 'James T. Kirk',
    'Discovery'   : 'Gabriel Lorca',
}

# Prints 'Benjamin Sisko'
print(captains['Deep Space 9'])

## ============================================================================
## Modules
## ============================================================================
##
## See also:
##     https://docs.python.org/3/tutorial/modules.html
##
## See also:
##     https://docs.python.org/3/reference/import.html
##
## As you've probably gathered by now, a lot of the code you will use will
## exist outside of the specific .py file you are working with. Some of these
## will be your own code. For example, you could run your previous
## "Hello, World!" script and pull in any variables defined therein by using
## an "import" statement like:

## Note: if you have difficulties with imports, look into "Python Path".

import hello_world

## There is a sample module that is creatively named "_7_sample_module.py".
## Feel free to open it and tinker with the functions and varibles inside:

import _7_sample_module

_7_sample_module.function()

## Alternatively, you can use Python's huge standard library to your heart's
## content (Python doesn't load them automatically because it doesn't know
## which ones you want):


import webbrowser

webbrowser.open('https://en.wikipedia.org/wiki/Rabbit_of_Caerbannog')

## ============================================================================
## Halp.
## ============================================================================
##
## If you need help, Python had a built-in help function:

list_1 = [1,2,3]
help(list_1)

## ============================================================================
## Questions?
## ============================================================================
## 
## On to _5_where_do_i_go_from_here.py ...
##

