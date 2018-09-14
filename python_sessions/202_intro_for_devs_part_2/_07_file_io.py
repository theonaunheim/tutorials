r'''
  __ _ _        _       
 / _(_) | ___  (_) ___  
| |_| | |/ _ \ | |/ _ \ 
|  _| | |  __/ | | (_) |
|_| |_|_|\___| |_|\___/ 

                        
'''
##=============================================================================
## Generally
##=============================================================================
##
## See also: https://docs.python.org/3/tutorial/inputoutput.html
##
## Writing to text files is fairly easy in Python, provided you understand
## the 'open()' function.
##
## For general use cases, you will only need two arguments:
##
## open(file, mode)
##
## See also: https://docs.python.org/3/library/functions.html#open

# For example:
with open('static/_07_/utf8.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        print(line)

## Your filename argument can be:
## 1. A relative filename such as '../Documents'
## 2. An absolute filename such as 'C:\Users\USERNAME\Documents\file.txt'
## 3. A file-like object or abstraction
##
## Your open type argument can be:
## 
## 1. 'r' for reading
## 2. 'w' for writing
## 3. 'a' for appending
##
## And the mode argument can have the following modifiers:
## 1. 'b' for binary (such as 'wb' to write a binary file)
## 2. '+' for opening a disk file (such as 'w+' to create and write).
## 3. 'x' for creating and failing if file exists.
## 4. 't' for text files (the default)
##
## There can also be combinations ...
with open('static/_07_/new_binary', 'wb+') as f:
    f.write(bytearray([0xa1, 0xb2, 0xc3, 0xd4, 0xe5, 0xf6]))

## Other common arguments are 'encoding' and 'errors'
##
## Python defaults to utf-8 encoding, which necessarily covers ASCII.
## Other encodings, however, such as the Windows CP-1252 or Latin 1
## require explicit coversion.
with open('static/_07_/cp1252.txt', encoding='cp1252') as f:
    print(f.read())

## If you anticipate encoding errors, you can specify what is done
## with any errors:
with open('static/_07_/cp1252.txt', encoding='ascii', errors='replace') as f:
    print(f.read())

with open('static/_07_/cp1252.txt', encoding='ascii', errors='ignore') as f:
    print(f.read())

with open('static/_07_/cp1252.txt', encoding='ascii', errors='strict') as f:
    print(f.read())

## Side note: for asynchonous IO, like file watchers see the 'asyncio' module.
##
##=============================================================================
## Abstractions
##=============================================================================
##
## You do not necessarily need to read from a file. For example,
## it is often more efficient to download something to RAM and then
## wrap it in a file like abstraction.
import io

# Create empty bytes IO.
file_like_object_bin = io.BytesIO()

# Create file like object
file_like_object_txt = io.StringIO('String file-like object.')

# Side note, you can nest if absolutely necessary.
# Open StringIO
with file_like_object_txt as f1:
    # Open BytesIO
    with file_like_object_bin as f2:
        # Read StringIO
        print(f1.read())
        # Write binary data, seek to zero, read data, and print.
        f2.write(bytearray([1, 1, 2, 3, 5, 8, 13, 21, 34, 55]))
        f2.seek(0)
        print(f2.read())

##=============================================================================
## Questions
##=============================================================================
