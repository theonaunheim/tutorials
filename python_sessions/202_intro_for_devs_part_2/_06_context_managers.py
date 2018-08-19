'''
                 _            _   
  ___ ___  _ __ | |_ _____  _| |_ 
 / __/ _ \| '_ \| __/ _ \ \/ / __|
| (_| (_) | | | | ||  __/>  <| |_ 
 \___\___/|_| |_|\__\___/_/\_\\__|
                                  
                                                 
 _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ ___ 
| '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__/ __|
| | | | | | (_| | | | | (_| | (_| |  __/ |  \__ \
|_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|  |___/
                             |___/               

'''
##=============================================================================
## Generally
##=============================================================================
##
## Often times there are pairs of activities or sets of activities that will
## go along with each other. An example of this would be that a program that
## opens a file should generally close that file when finished. Another
## example would be that a database connection that a program opens should
## probably be closed and committed. In order to make this process easier,
## and to avoid the problems that go along with forgetting these processes,
## Python has the 'with' statement.
##
## For more on the 'with' statement:
## https://docs.python.org/3/reference/compound_stmts.html#with
##
## These "with" clauses are known as context managers.

# One can open a file with the open command, read it, and then close it:
file_obj = open('static/_06_/file_1.txt', 'r')
file_data = file_obj.read()
print(file_data)
file_obj.close()

# Using a context manager, we can automatically close the file when done:
with open('static/_06_/file_2.txt', 'r') as f:
    data = f.read()
    print(data)

# The action taken when exiting the scope is defined by the behavior
# of the object's __enter__/__exit__ magic methods.


class Contexty(object):
    def __enter__(self):
        print('Entering context manager.')
    def __exit__(self, exc_type, exc_value, traceback):
        # Exit needs to handle exceptions.
        print('Exiting context manager.')


with Contexty():
    garbage = input('Now inside context manager. Press a key.')

##=============================================================================
## Questions
##=============================================================================
