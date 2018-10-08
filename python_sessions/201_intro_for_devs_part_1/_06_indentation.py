'''
  _           _            _        _   _
 (_)_ __   __| | ___ _ __ | |_ __ _| |_(_) ___  _ __
 | | '_ \ / _` |/ _ \ '_ \| __/ _` | __| |/ _ \| '_ \
 | | | | | (_| |  __/ | | | || (_| | |_| | (_) | | | |
 |_|_| |_|\__,_|\___|_| |_|\__\__,_|\__|_|\___/|_| |_|


Before we begin: "A Whitespace Haiku", by Teddy K:

    Tabs in Python code? 
    You may want to rethink that.
    People will hate you.

PLEASE DO NOT MIX SPACES AND TABS.

'''
##=============================================================================
## Generally
##=============================================================================
##
## Most computing languages have scope, code blocks, or units or units of
## executable code. In most languages, these code blocks are delimited through
## the use of curly braces ('{}'). For example, in C a conditional statement
## might look like:
##
##     int var_1;
##     var_1 = 10;
##     if (var_1 > 5) {
##        int var_2;
##        printf("This code is executed because the condition is met!");
##        printf("This is also executed because it's part of a block!");
##        var_2 = 20;
##     }
##
## Unlike other languages, Python uses indentation to delimit code blocks.
## The general rule is that everything indented at the same level is a part of
## that particular block.
 
var_1 = 10

if var_1 > 5:
    print("This code is executed because the condition is met!")
    print("This is also executed because it's part of a block!")
    var_2 = 20

## Note: if you come from a language like C or C++, you should note that code
## blocks do not limit scope, aside from function or class definitions. In the
## C example above, var_2 would disappear after the (var_1 > 5) block was
## finished. In Python, var_2 would stick around.
##
## Other computer languages also have the concept of statements. These are a
## single unit of execution, like the following in C:
##
##     printf("W00T!");
##
## In C, these are delimited with a semi-colon (';'). Python uses newlines.
##
##=============================================================================
## The takeaway
##=============================================================================
##
## In Python, whitespace is syntactically significant. Python uses whitespace
## to define things like function and condition scope. If something is
## improperly indented, it simply won't work--it is an error to indent
## unnecessarily.
##
## I'm not going to lie to you. This is weird for most people and it takes some
## getting used to. That said, most of the people I know who code frequently in
## Python actually appreciate the fact that Python code will look similar from
## user-to-user, and the lack of curly braces makes the source cleaner and
## easier to read.
##
##=============================================================================
## So what needs to be indented?
##=============================================================================
##
## In short, compound statements need to be indented. Compound statements are
## statements that necessarily apply to a number of subsequent statements.
## They start with a line ending in a colon (':') and end when the indented
## section stops.
##
## Note: the colon is also used for dictionaries to separate keys and values:
## {'key': 'value'}, and for lambdas (e.g. lambda x: x +1), and for array
## slicing (e.g. my_array[2:5]).
##
## See also: https://docs.python.org/3/reference/compound_stmts.html
##
## Some examples of compound statements are:
##
##=============================================================================
## Definitions
##     def: defines functions
##     class: defines classes
##=============================================================================


def my_function():
    a = 5
    b = 6
    return 7


class MyClass(object):

    class_attribute = 5

    def my_method(self):
        a = 5
        b = 6


# Side note: you will often see things like:
def noop_function():
    pass


## 'pass' is the no-op keyword. It does nothing. It is generally used to make
## sure that code doing nothing can be interpreted. If we were to write the
## above as:
##
##     def noop_function():
##
## ... without a following statement, Python would have no idea where the
## function ended (i.e. it never got an unindented line to let it know where
## the function scope ended.
##
##=============================================================================
## Conditionals
##     if: simple conditional
##     elif: compound conditional
##     else: compound conditional
##=============================================================================

a = 'SI'

if a == 'SI':
    print("Nobody expects the Spanish Inquisition!")

    if 'S' in a:
        print("Yes, definitely Spanish...")

elif a == 'LJ':
    print("He's a lumberjack and he's okay!")
    print("He sleeps all night and he works all day!")

else:
    print("I don't recognize this string!")

## Note: many Python was named after "Monty Python's Flying Circus", which is
## why you will see many Monty Python jokes.
##
##=============================================================================
## Loop
##     for: iteration based loop
##     while: conditional based loop
##=============================================================================

for elem in ['this', 'parrot', 'is', 'no', 'more']:
    upper = elem.upper()
    print(upper)

print("This parrot wouldn't *voom* if I 4,000 volts through it!")

var = 10
while var > 0:
    print(var)
    var = var - 1


##=============================================================================
## Exceptions:
##     try: enter a try block
##     except: catch exception block
##     finally: try termination statement
##=============================================================================

try:
    a = 5
    b = 6
    print(nonexistant_variable)
except NameError:
    print("Error!")
finally:
    print("Cleanup code here!")

# Context:
#     with: context manager, use varies.
with open('_01_intro.py', 'r') as f:
    print("Looking at linecount.")
    print(len(f.readlines()))


##=============================================================================
## Line breaks
##=============================================================================

# Actual line breaks can be accomplished in a variety of ways. Within
# delimiters, whitespace is not significant.
longcat_str = 'Longcat is looooooooooooooooooooooooooooooooooooooooooooooooo' \
'oooooooooooong.'

longcat_str = ('Longcat is looooooooooooooooooooooooooooooooooooooooooooo'
                  'oooooooooooong.',
)

my_dict = {
    'Norwegian Blue': 'a late parrot',
    'Macaw': 'gone to meet its maker'
}

## So to qualify our previous rule: whitespace is always significant ...
## unless it's not. Delimiters like (), [], and {} may make it insignificant.
##
##=============================================================================
## Questions?
##=============================================================================

