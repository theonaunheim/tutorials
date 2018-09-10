'''
   __ _                                 _
  / _| | _____      __   __ _ _ __   __| |
 | |_| |/ _ \ \ /\ / /  / _` | '_ \ / _` |
 |  _| | (_) \ V  V /  | (_| | | | | (_| |
 |_| |_|\___/ \_/\_/    \__,_|_| |_|\__,_|

                      _ _ _   _                   _
   ___ ___  _ __   __| (_) |_(_) ___  _ __   __ _| |___
  / __/ _ \| '_ \ / _` | | __| |/ _ \| '_ \ / _` | / __|
 | (_| (_) | | | | (_| | | |_| | (_) | | | | (_| | \__ \
  \___\___/|_| |_|\__,_|_|\__|_|\___/|_| |_|\__,_|_|___/

'''
##=============================================================================
# Generally
##=============================================================================
##
## Python is largely consistent with other languages when it comes to control
## flow and conditional execution. Here we're going to tackle the basics of
## what is available to the programmer.
##
## See also: https://docs.python.org/3/tutorial/introduction.html
## See also: https://docs.python.org/3/tutorial/controlflow.html
##
##=============================================================================
# Loops
##=============================================================================
##
## Python has two main loop types, the 'for' loop, which is iteration based,
## and the 'while' loop, which is condition based.
##
##=============================================================================
## For Loop
##=============================================================================

# Here are some for-loops:

for offering in ['shrubberry', 'another shrubbery', 'herring']:
    print("We want a {}!".format(offering))

# We will get to the 'range' keyword later, which generates number ranges.
for n in range(10):
    print(n)

## For loops are based on iteration. They use the 'for' and 'in' keywords to
## go through each and every item of something one item at a time.

# The basic form is:
iterable = [1, 2, 3]

for element in iterable:
    # do_stuff()
    pass

## So for each item of collection_of_items you can process the
## individual item by referencing the name you gave it.
##
## Warning: ranges in Python are open/inclusive at the low end and
## closed/exclusive at the high end.

## Warning: the 'in' operator is used in two different ways.
##
## >>> 1 in [1, 2, 3]
## True
##
## >>> for x in range(10):
## ...     pass

# Combining the two techniques...
for index, offering in enumerate(['shrubberry', 'another shrubbery', 'herring']):
    print("Offering #{}: {}".format(index, offering))

##=============================================================================
# While Loop
##=============================================================================

# Here are some while loops.

index = 0
while index != 10:
    print(str(index) + ' is not 10. Condition is True. Loop will continue.')
    index = index + 1

# Infinite loop idiom.
while True:
    pass

## While loops are based on conditions. At the top of each loop, the loop
## checks whether the condition is True. If it is True, it continues. If it
## is False, the loop stops. The basic form is:
##
## while BOOLEAN_CONDITION:
##     LOOP_BODY
##
## Other languages may no longer track items created in loops. In Python,
## however, these items will stick around:

for x in range(0,10):
    my_integer = x

print(f'The last value of my integer was {my_integer).')

##=============================================================================
## Loop Flow
##=============================================================================
##
## Sometimes while going through a loop, it becomes necessary to jump to the
## top of the loop, completely exit the loop, or perform some action or
## cleanup when the loop completes successfully. Python uses the keywords
## 'continue', 'break', and 'else' for these situations respectively.

## "break" keyword
##
## If you want to cease the loop where it is and immediately break out of it,
## you can use the break statement.
for bird in ['duck', 'duck', 'goose', 'duck']:
    print(bird)
    # Here, the 3rd time we run through the loop, we will trip the break.
    if bird == 'goose':
        # The last duck will never print.
        break

## "continue" keyword
##
## If we do not totally want to break out of the loop, but it makes no sense
## to run the loop all the way to the end, we can use a continue statement.
for bird in ['duck', 'duck', 'goose', 'duck']:
    # The third time through, we start back at the top of the
    # loop with the next bird.
    if bird == 'goose':
        # Goose will never print.
        continue
    print(bird)

## 'else' keyword
##
## This is not to be confused with the 'else' used with 'if' and 'elif'. If
## you want to ensure that certain code is run when the loop completes
## successfully, but not with a break, use else.
for bird in ['duck', 'duck', 'duck']:
    if bird == 'goose':
        break
else:
    print("Loop completed successfully with no geese.")

# Compare this with:

for bird in ['duck', 'duck', 'goose']:
    if bird == 'goose':
        break
else:
    print("Loop completed successfully with no geese.")

##=============================================================================
## Conditionals
##=============================================================================
##
## As you've already seen, it's impossible to do anything useful without
## some sort of conditional logic. Python uses the keywords 'if', 'elif', and
## 'else' to address these issues.
##
## 'if' keyword
##
## if analyzes a boolean condition. If it evaluates to True, the interpreter
## will run the code within the block. If it evaluates to False, the
## interpreter will not run the code within the block.
solution_found = True
count = 15

if count > 15:
    print("The count is greater than 15!")

if count > 15 and solution_found is True:
    print("The count is greater than 15 and solution found!")


## 'elif' keyword
##
## elif is used as a follow-up to if. Presuming the prior if (or any elifs
## in place, if applicable) do not resolve to True, the elif is executed.
##
    
# This evaluates to False.
if count < 10:
    # Because it evaluates to False it will not execute.
    print("Count is less than 10")

# This is evaluated because the previous was not True.
elif count < 19:
    # Because this evaluates to True, it will print.
    print("Count is less than 19")

# This will never be evaluated.
elif count < 18:
    # Because never evaluated, it never gets an opporutnity to execute.
    print("Count is less than 18")

## 'else' keyword
##
## 'else' is the last item following an 'if' or series of 'elif' statements.
## if none of the 'if' or 'elif' statements in the prior chain execute, the
## 'else' will executed.

count = 7

# Python also helpfully supports ranging comparison for more compact checks
if -2 < count < 9:
    print("Count is between -2 and 9, inclusive.")
else:
    print("Triggering else block.")

##=============================================================================
## Caveat
##=============================================================================
##
## Things that evaluate boolean conditions like "if" and "while" will
## implicitly coerce non-booleans using the __bool__() magic method. In other
## words:
##
## while 1:
##     pass
##
## ... is actually:
##
## while bool(1):
##     pass
##
## Some of the more common boolean conversions are below:

# Numbers are False if zero and True if anything else.
bool(0)        # False
bool(0.0)      # False
bool(3)        # True
bool(-20)      # True

# Sequences (including strings) are false if they are length 0. Otherwise true.
bool([1,2,3])  # True
bool([])       # False
bool('\0')     # True (even null string has length of 1)
bool('Bam!')   # True

# Other objects and instances will generally be True.
bool(object()) # True
bool(int)      # True

# Except for None, which is always false
bool(None)     # False

## To summarize:
##     1) None is False
##     2) Zero is False
##     3) Zero length sequence or string is False
##     4) Everything else is True
##
## Mnemonic: "nothing is False"
##
##=============================================================================
## Questions?
##=============================================================================

