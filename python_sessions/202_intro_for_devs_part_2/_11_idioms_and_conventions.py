'''
 _     _ _                                       _ 
(_) __| (_) ___  _ __ ___  ___    __ _ _ __   __| |
| |/ _` | |/ _ \| '_ ` _ \/ __|  / _` | '_ \ / _` |
| | (_| | | (_) | | | | | \__ \ | (_| | | | | (_| |
|_|\__,_|_|\___/|_| |_| |_|___/  \__,_|_| |_|\__,_|
                                                   
                                _   _                 
  ___ ___  _ ____   _____ _ __ | |_(_) ___  _ __  ___ 
 / __/ _ \| '_ \ \ / / _ \ '_ \| __| |/ _ \| '_ \/ __|
| (_| (_) | | | \ V /  __/ | | | |_| | (_) | | | \__ \
 \___\___/|_| |_|\_/ \___|_| |_|\__|_|\___/|_| |_|___/
                                                      

'''
##=============================================================================
## Generally
##=============================================================================
##
## Python has a bunch of common idioms and conventions that are described as
## "Pythonic". This is a quick refresher on some of the common items.
##
## See: https://jeffknupp.com/writing-idiomatic-python-ebook/
## See: https://www.python.org/dev/peps/pep-0008/
##
##=============================================================================
## PEP8 stuff
##=============================================================================


class SampleClass(object):
    '''Classes are Pascal case.
    
    Doc strings are typically formatted something like this. Generally
    getters and setters are frowned upon. Methods are generally separated
    by a single line. Classes and module functions are typically separated
    by two lines.
    
    '''

    def __init__(self):
        '''This is how you should document things.'''
        self.attribute_1 = 'Public attributes are lower case.'
        self._attribute_2 = 'Private attributes have underscore prefix.'

    def method_1(self):
        '''Public methods are lower case.'''
        var_1 = 'function and method variables are lower case.'

    def _method_2(self):
        '''Private methods are prefixed with an underscore.'''
        pass

    def set_attribute_1(self):
        '''Python frowns upon getter and setter methods.'''
        raise NotImplementedError()


##=============================================================================
## Other idioms
##=============================================================================
##
## Your application's entry point should generally have something like this:
##
## def main():
##     pass
##
## if __name__ == '__main__':
##     main()

def main():
    print('You will often see this notation for a main entry point.')
    print('What this is doing is defining a main function.')
    print('This main function is intended to be executed.')
    print('But it can also be imported.')
    print('Remember, __name__ will only equal __main__ in one place.')
    print('And thats the script that is being executed.')


print('So this will get executed and main() will be defined.')
if __name__ == '__main__':
    print('But this will only get executed if run from interpreter.')
    main()

# Tuple unpacking if we assign a tuple
my_tuple = ('Theo', 'Keith', 'Naunheim')

# That can implicitly be split during an assignment
first, middle, last = my_tuple
print(first)

# This has implications for comprehensions
for_dict = {'a': 1, 'b': 2, 'c': 3}
rev_dict = {value: key for key, value in for_dict.items()}
print(rev_dict)

# The ever so useful zip() function
list_1 = ['Alice', 'Bob', 'Charlie']
list_2 = ['Anderson', 'Brown', 'Chevers']

for first, last in zip(list_1, list_2):
    print('Welcome, {} {}!'.format(first, last))

# And forms the basis of how Python does numbered indices
for index, flavor in enumerate(['Chocolate', 'Vanilla', 'Strawberry']):
    print(str(index) + ': ' + flavor)

# Python doesn't have case. Use dictionaries instead. Everything is an object.
def func_1():
    print('Triggering func_1')


def func_2():
    print('Triggering func_2')


def func_3():
    print('Triggering func_3')

func_dict = {1: func_1, 2: func_2, 3: func_3}

entry = int(input('Enter 1, 2, or 3\n[!] '))

function = func_dict[entry]
function()

##=============================================================================
## Questions
##=============================================================================
