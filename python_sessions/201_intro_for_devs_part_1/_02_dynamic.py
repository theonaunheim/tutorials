'''
      _                             _
   __| |_   _ _ __   __ _ _ __ ___ (_) ___
  / _` | | | | '_ \ / _` | '_ ` _ \| |/ __|
 | (_| | |_| | | | | (_| | | | | | | | (__
  \__,_|\__, |_| |_|\__,_|_| |_| |_|_|\___|
        |___/

'''
##=============================================================================
## Generally
##=============================================================================
##
## Python generally strikes a pretty good balance between efficiency and
## usability. There are a couple things about Python you should be aware of
## some of these tradeoffs before we even get to the idiosyncracies of the
## language.
##
##=============================================================================
## Python is interpreted
##=============================================================================
##
## When you installed Python, you got a python.exe on your computer. This
## Python executable is actually used to run any Python file (or collection of
## files). This contrasts with compiled languages like Java, C++, or C#. This
## benefits you, the programmer, because the try/fail workflow process is often
## the quickest and most efficient way to find working solutions.
##
## The drawback of the flexibility the language provides is that Python
## programs generally aren't as fast as compiled programs. Python generally can
## do what you want it to, but it isn't the solution to every problem.
##
## Note: compiled/interpreted dichotomy isn't quite as black and white as we're
## making it out to be. With a few exceptions, languages aren't completely
## interpreted or completely compiled. But that's beyond the scope of our
## conversation today.
##
## Get to know your interpreter! In addition to using this admittedly deficient
## IDE, you can use Python from the command line. If you've added it to your
## PATH, you can simply open up a terminal and type 'python'.
##
##=============================================================================
## Python is dynamically typed.
##=============================================================================
##
## Some languages are picky about the types that specific variables can hold.
##
## For example, in the C language:
##
##     char c;
##     c = 'Z';
##     c = 500;
##
## This variable 'c' points to a block of memory big enough for a character.
## If you wanted to put something else in there like the number 500, your
## compiler would throw a fit. This is what we call 'static typing', which is
## a behavior that many languages that enforce compile-time checks exhibit.
##
## See also: https://en.wikipedia.org/wiki/Type_system#Static_type_checking
##
## It benefits a language because it requires minimal runtime support and
## promotes type safety (e.g. using variables like they are supposed to be
## used).
##
## On the other end of the spectrum, Python doesn't care what you put in a
## variable.

var = 1
var = var + 5
var = {'key': 'value'}
var = [1, 2, 3, 4, 5]
print('No errors so far!')

## If you want to put a class in a variable, Python supports that. If you
## want to assign a function to a variable and then put that function inside
## a list, go for it. Python don't care. While this makes your life easier
## for the most part, it can result in problems.

# Say I have a name that I point at a number ...
score = 90

# I can do whatever I want with the number ...
percent = x / 100.0

# ... until I do something un-number-like with it!
plz_no = x / 'rutabaga'

## The interpreter is understandably confused at this point, because it has
## no idea how to divide 90 by 'rutabaga'. It's nonsensical, so it will raise
## a TypeError, which essentially means you did something with a type that you
## shouldn't have.
## 
##=============================================================================
## Everything Is An Object
##=============================================================================
##
## You may be familiar with object-oriented programming. In Python, you are
## doing object-programming whether you like it or not. Pretty much everything
## that is not a keyword or an operator is an object. Again, whether it is an
## integer, or a string, or a float ... the Python interpreter view it as an
## object. We will often use the dir() command to inspect objects to take a
## look at their methods and attributes.

# For example, say we have a variable pointing at an integer.
x = 5
print(dir(x))

# This simple integer has a bunch of attributes and methods attached to it.
# It is a full-fledged object. We access attributes and methods using the
# period ('.') operator. Similarly, a basic string has a bunch of things you
# can do to it:
s = 'The Ministry of Silly Walks'
print(s.upper())
print(type(s))

# Similarly functions, classes, methods, attributes, etc, are all types:
print(type(type))
print(type(s.upper))

l = ['And', 'now', 'for', 'something', 'completely', 'different', 42, [':-D']]
print(dir(l))

## This can be a bit worrisome at first, but in the long run it will make your
## life easier.
##
##=============================================================================
## Garbage Collected
##=============================================================================
##
## Finally, Python is garbage collected. If you're not familiar with this,
## don't worry about it. All it means is that you don't have to manually
## manage memory like you would with C or C++. If you're done with something
## and it will never be used again, it will simply be disposed of. Python uses
## reference counting instead of tracing garbage collection for historical
## reasons.
##
## Note: you will almost never have to delete anything using the 'del'
## keyword, with the exception being the deletion of keys from dictionaries.
## If you want to prompt the garbage collector to take a large item, simply
## assign the None object to it.
quote = "And like that, poof. He's gone."

# The string will be garbage collected.
quote = None

##=============================================================================
## Questions?
##=============================================================================

