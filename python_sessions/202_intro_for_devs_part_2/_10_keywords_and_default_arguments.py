'''
 _                                    _                       _ 
| | _____ _   ___      _____  _ __ __| |___    __ _ _ __   __| |
| |/ / _ \ | | \ \ /\ / / _ \| '__/ _` / __|  / _` | '_ \ / _` |
|   <  __/ |_| |\ V  V / (_) | | | (_| \__ \ | (_| | | | | (_| |
|_|\_\___|\__, | \_/\_/ \___/|_|  \__,_|___/  \__,_|_| |_|\__,_|
          |___/                                                 
     _       __             _ _   
  __| | ___ / _| __ _ _   _| | |_ 
 / _` |/ _ \ |_ / _` | | | | | __|
| (_| |  __/  _| (_| | |_| | | |_ 
 \__,_|\___|_|  \__,_|\__,_|_|\__|
                                  
                                            _       
  __ _ _ __ __ _ _   _ _ __ ___   ___ _ __ | |_ ___ 
 / _` | '__/ _` | | | | '_ ` _ \ / _ \ '_ \| __/ __|
| (_| | | | (_| | |_| | | | | | |  __/ | | | |_\__ \
 \__,_|_|  \__, |\__,_|_| |_| |_|\___|_| |_|\__|___/
           |___/                                    

'''

##=============================================================================
## Generally
##=============================================================================
##
## As you've seen, arguments are pretty simple. You just put them in
## when you define your function and when you call your function. But what
## if you want to use variable length arguments, default arguments, or
## keyword arguments?
##
## https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
##
##=============================================================================
## Default and Keyword arguments
##=============================================================================
##
## We define default arguments using the equal sign after a parameter.
## Note: keyword arguments must come after regular arguments. These
## are called keyword arguments or kwargs. You only need to list the
## keyword arguments you actually want to change. Otherwise, they
## will take their default value.

import time

def hello(punctuation, name='Unspecified Person', delay=.01):
    time.sleep(delay)
    print('Hello, ' + name + punctuation)


hello('!', 'Tito')
hello('.', name='Jermaine')
hello('?', delay=2)

# Note, you can omit keyword args, but not regular args.
try:
    hello(name='Michael')
except TypeError as e:
    print(e)

# Where keyword arguments really shine is when you have a bunch of arguments.
def onerous_func(one=1, two=2, three=3, four=4):
    print('{} -> {} -> {} -> {}'.format(one, two, three, four))


# Because instead of typing out:
onerous_func(5,6,7,8)
onerous_func(9,10,11,12)

# We can use dictionaries using the ** notation, which expands the dict
# and transforms it into keywords.
argument_dict = {
    'one': 900,
    'two': 1000,
    'three': 1500,
    'four': 2000
}

onerous_func(**argument_dict)

# Note that you can do the same thing with lists using the * notation.
argument_list = [5000, 100000, 'how did i get here i am not good with computer', 2000]

onerous_func(*argument_list)

## If you want to get fancy, take a look at decorators and functools.partial.
##
## See: https://docs.python.org/3.7/library/functools.html#functools.partial
## See: https://www.python.org/dev/peps/pep-0318/
##
##=============================================================================
## Questions
##=============================================================================
