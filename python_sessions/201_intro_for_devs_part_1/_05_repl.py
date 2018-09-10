'''
                 _
  _ __ ___ _ __ | |
 | '__/ _ \ '_ \| |
 | | |  __/ |_) | |
 |_|  \___| .__/|_|
          |_|
'''
##=============================================================================
## Generally
##=============================================================================
##
## See also: https://docs.python.org/3.7/tutorial/interpreter.html
## See also: https://en.wikipedia.org/wiki/Read–eval–print_loop
##
## So, if we wanted to we could always edit a source file and then run it like
## we did for "my_hello_world.py". For our presentation, however, it's going to
## be much simpler if we just use Python's build in Read-Eval(uate)-Print Loop
## (abbreviated REPL). Instead of reading a file line-by-line, the REPL enables
## us to execute statements by:
##
## 1. Reading input that we type in;
## 2. Evaluating the statement that we put in after pressing enter;
## 3. Printing any results; and,
## 4. Loops back to step 1.
##
## Why would you ever want to do that? After all, if you're typing commands in
## yourself, you're losing the best part of using computers (i.e. making the
## computer do all the work). The answer is that REPL'ing is a great way to
## debug and test as you go.
##
##=============================================================================
## REPL'ing
##=============================================================================
##
## So let's try out the REPL. Go to the command prompt and type 'python' by
## itself, without adding a filename. Entering the Python command without a
## filename is how you trigger the REPL. We will be typing/cutting/pasting
## commands into the REPL (in PowerShell, not in IDLE) for the remainder of
## this session.
##
## Some useful REPL-specific commands:
## 1. help(): this provides a general help command.
## 2. quit(): this exists the repl.
##
##=============================================================================
## Example
##=============================================================================

# Copy this command and paste it into the interactive terminal and hit enter.
# Again, do not use IDLE's shell. Use PowerShell or CMD.

a = 5
if a > 1:
    print("a is greater than 1.")

## It should look something like this:
##
## >>> a = 5
## >>> if a > 1:
## ...     print('a is greater than 1.')
## ...
##
## Notice that when something is indented (which we will get to later) the
## we see a series of dots instead of arrows. This indicates that you are in
## the middle of something that is not yet complete.
##
## Press enter once (or twice if need be). You should get a statement that
## 'a is greater than 1'.

# Now let's try typing it in directly. Type in:
b = 7
a + b

## Unless explicitly told to print, the REPL will only give you the return
## value from the last statement. Feel free to experiment with the REPL as we
## continue through the presentation.
##
##=============================================================================
## Questions?
##=============================================================================

