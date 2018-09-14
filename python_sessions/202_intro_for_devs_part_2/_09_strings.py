'''
     _        _                 
 ___| |_ _ __(_)_ __   __ _ ___ 
/ __| __| '__| | '_ \ / _` / __|
\__ \ |_| |  | | | | | (_| \__ \
|___/\__|_|  |_|_| |_|\__, |___/
                      |___/     

'''

##=============================================================================
## Generally
##=============================================================================
##
## Strings in Python are full fledged objects. They are denoted by the use
## of single quotations (') or double quotations ("). Backslash is used for
## escape sequences. Multiline strings are denoted with (''').
##
## See: https://developers.google.com/edu/python/strings
## See: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

# Concatenating strings can be done in a variety of manners.
basic_string = 'Bye, ' + 'Felicia' + '.'
basic_string = (
    'Bye, '
    'Felicia'
    '.'
)
basic_string = ''.join(['Bye, ', 'Felicia', '.'])

# You can convert to string using a functional "cast"
one_int = str(1)
one_float = str(1.0)

## Strings are on of the most important types within Python, and
## consequently, they are built out with a lot of methods and attributes
## that you can use.
string_methods = [
    'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
    'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
    'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
    'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
    'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
    'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
    'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
]

## Strings in Python (version 3 and above) default to UTF-8. You
## 'decode()' bytes to turn them into strings. You 'encode()' strings
## to turn them into bytes. Mnemonic: B is closer to D. Bytes are
## Decoded. S is closer to E. Strings are Encoded.
ascii_bytes = bytes([
    0x54, 0x68, 0x65, 0x20, 0x71, 0x75, 0x69, 0x63, 0x6b, 0x20,
    0x62, 0x72, 0x6f, 0x77, 0x6e, 0x20, 0x66, 0x6f, 0x78, 0x20,
    0x6a, 0x75, 0x6d, 0x70, 0x65, 0x64, 0x20, 0x6f, 0x76, 0x65,
    0x72, 0x20, 0x74, 0x68, 0x65, 0x20, 0x6c, 0x61, 0x7a, 0x79,
    0x20, 0x64, 0x6f, 0x67
])

plaintext = ascii_bytes.decode('ascii')
print(plaintext)

binary = 'The lazy dog jumped over the quick brown fox'.encode('latin-1')
print(binary)

##=============================================================================
## Formatting strings
##=============================================================================
##
## See: https://docs.python.org/3.6/library/string.html#format-string-syntax
##
## Formating strings is worth a topic all on its own. It's got its own
## mini-templating language. In general, you'll want to use the basic string
## formatting syntax:

name_and_age = {
    'Steve': 9,
    'David': 30,
    'Faye': 15
}

# This can be done on a keyword basis.
kw_template_string = '{name_input} is {age_input} years old.'

for name, age in name_and_age.items():
    print(kw_template_string.format(name_input=name, age_input=age))

# This can be done on a positional basis.
pos_template_string = '{} is {} years old.'

for name, age in name_and_age.items():
    print(pos_template_string.format(name, age))

# And it can be done directly to a string
print('This string needs no variable, {}.'.format('yo'))

# Or it can be done with formatting strings.
a = 'Steve'
print(f'{a} is a good friend of mine.')

##=============================================================================
## String methods
##=============================================================================

# Some of the more useful string methods are:

# Upper
print('Name'.upper())

# Lower
print('Name'.lower())

# Endswith
print('Ms. Butterworth'.endswith('worth'))

# __in__
print('Ruta' in 'Rutabaga')

# len()
print(len('Stringy'))

# isalpha, isnumeric, isalnum
print('21'.isnumeric())

# strip
print('    get rid of whitespace     '.strip())

# replace (for more power, see the regex module 're'
print('replaced'.replace('e', '!'))

# join
print(','.join(['string1', 'string2', 'string3']))

# split
print('a,b,c,d,e,f,g'.split(','))

# find
print('the quick brown fox'.find('fox'))

# partition, a personal favorite
start, splitter, end = 'Split the string here and do stuff'.partition('here')
print(start)
print(splitter)
print(end)

##=============================================================================
## Special characters
##=============================================================================

print('''
    \n Line Feed 
    \r Carriage Return 
    \r\n Carriage Return + Line Feed 
    \v Vertical Tab
    \t Tab
    \f Form Feed 
''')

##=============================================================================
## Questions
##=============================================================================
