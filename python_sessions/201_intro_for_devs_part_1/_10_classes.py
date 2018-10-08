'''
       _
   ___| | __ _ ___ ___  ___  ___
  / __| |/ _` / __/ __|/ _ \/ __|
 | (__| | (_| \__ \__ \  __/\__ \
  \___|_|\__,_|___/___/\___||___/

'''
##=============================================================================
## Classes
##=============================================================================
##
## https://docs.python.org/3/tutorial/classes.html
##
## Classes are the foundation of object-oriented programming. Like functions,
## classes are pretty easy to work with. We're going to breeze through this
## fairly quickly, as people on the data analysis side of things will likely
## never use these. Be forewarned this is a much more complicated topic than
## we're making it out to be.
##
##=============================================================================
## Defining Classes
##=============================================================================


class BasicObject(object):
    '''Class documentation here.'''
    
    def __init__(self):
        self.attribute_1 = 'Basic attribute'

    def method(self, arg_1):
        print('I am a method taking an argument: ' + str(arg_1))
        print('I can reference ' + self.attribute_1)
        return 'Return value'


## Lets break this down ...
##
## class BasicObject(object):
##
## Here we define an class BasicObject. This class inherits from Python's base
## 'object' type. This is the default, and we simply mention it to be explicit.
## After we put togther the name and parent classes, we define our __init__()
## method.
##
##    def __init__(self):
##        self.attribute_1 = 'Basic attribute'
##
## For reasons we're not going to concern ourselves with here, you as the
## programmer do not have direct control over object creation (which is done)
## with the __new__() method. You have to settle for an __init__() method,
## which sets up the instance of the object immediately after creation. Notice
## that the first argument for any method bound to a class will be a reference
## to the instance itself, which by convention is called 'self'. Your
## __init__() method allows you to bind attributes indicated with ('.') or
## dot notation. In short, this initializer takes no arguments and attaches
## a string to attribute_1.
##
##
## If you intend to call the constructor of the class you inherited from, you
## will want to call super().__init__() on as the first line of your __init__()
## function, and pass super()__init__() any required arguments.
##
##    def method(self, arg_1):
##        print('I am a method taking an argument: ' + arg_1)
##        print('I can reference ' + self.attribute_1)
##        return 'Return value'
##
## This is a method. Like __init__() its first argument is a reference.
## Therefore, by definition it can only be used after we have created an
## instance. It needs to be instantiated.


class FancyObject(object):
    '''Docstring.'''

    cls_attribute = 'I am shared between all instances of this class!'

    def __init__(self, arg_1, arg_2):
        self.attribute_1 = arg_1
        self.attribute_2 = arg_2
        self._private = 'Private attributes should be prefixed with _'
        self.public = 'Public attributes need no underscore.'
        super().__init__()

    def __str__(self):
        '''This is a magic method.'''
        return 'FancyObject Instance!'

    def _priv_method(self, arg_1):
        print(arg_1)

    def pub_method(self, arg_1):
        self._priv_method(arg_1)

    def setAttribute1(self, my_input):
        print("Do not use getters and setters.")
        print("Guido van Rossum frowns on this.")

    # This is decorator syntax. We're not getting into this.
    @classmethod
    def class_method(cls, arg_1):
        print("As a class method, I have access to class attributes!")
        print("Like " + cls.cls_attribute)


##=============================================================================
## Instantiating and Using Classes
##=============================================================================
##
## We instantiate our class, which gives us the ability to use it. For example,
## if we wanted to use BasicObject:

# We would instantiate it.
basic = BasicObject()

# And then use its methods.
return_value = basic.method(5)

# We can instantiate items that require initial arguments
fancy = FancyObject(1, 2)

# And we can then use its methods.
fancy.pub_method(5)

##=============================================================================
# Inherentance / Polymorphism / Encapsulation
##=============================================================================
##
## 1. Multiple inheretance is permitted, but frowned upon.
## 2. All methods are virtual and polymorphism is straightforward.
## 3. Encapsulation isn't enforced.


# An example of name-mangling
class A(object):
    def __init__(self):
        pass

    def __say_hello():
        print("Hello, world!")


class B(A, object):
    '''Not only is this nonsensical, multiple inherentence is frowned on.'''
    def __init__(self):
        pass

    def __say_hello():
        print("Hallo, Welt!")


##=============================================================================
## Questions?
##=============================================================================

