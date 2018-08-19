'''
  _
 | |_ _   _ _ __   ___  ___
 | __| | | | '_ \ / _ \/ __|
 | |_| |_| | |_) |  __/\__ \
  \__|\__, | .__/ \___||___/
      |___/|_|
'''
##=============================================================================
## Generally
##=============================================================================
##
## Note: this is a lot of material at one time. You're not expected to
## completely understand this. It's more for reference than anything else.
##
## See also: https://docs.python.org/3/library/stdtypes.html
##
## Python has a lot of standard types built in for you to use. Unimaginatively,
## these are named 'builtins'. Here is a brief tour of builtins.
##
##=============================================================================
## None Type
##=============================================================================

examples = [None]

# For nothing/null/missing values there's a special data type called None
empty_var = None
big_var = 'I am a big variable that is no longer needed and can be trashed'
big_var = None


##=============================================================================
## Boolean types
##=============================================================================

examples = [True, False]

# For truthiness and falsity, we have booleans True and False:
1 + 1 == 3
no_1_curr = True
if no_1_curr:
    print('Throw your hands in the ur.')

##=============================================================================
## Numeric types
##=============================================================================

examples = [int, float, complex]

# For integers we have integers.
1 + 2

# For partial numbers, we have floats (decimals are a separate lib.)
1.0 / 3.0

# Note: most conversions should be done for you automatically.
1 / 3

##=============================================================================
## Range Type
##=============================================================================
examples = [range]

# Range types are a special type for generating a list of numbers.
for x in range(0, 10, 2):
    print(x)

list(range(0, 30, 3))

##=============================================================================
## Binary types
##=============================================================================

examples = [bytes, bytearray, memoryview]

# These are for dealing with binary data.
bytes([0x04])
bytearray([0x04, 127, 0xff])
memoryview(b'string')

##=============================================================================
##  Other Types
##=============================================================================

import types


# Iterator types covered in generators and comprehension.
examples = [iter]

# Sequence types covered in containers.
examples = [list, tuple, dict, set, frozenset]

# Strings covered in string section.
examples = [str]

# Modules and packages are dealt with in the packages and modules section
examples = [types.ModuleType]

# Functions are dealt with in the function section
examples = [types.FunctionType]

# Classes and methods are dealt with in the classes section.
examples = [types.ClassType, types.MethodType]

##=============================================================================
## Questions?
##=============================================================================

