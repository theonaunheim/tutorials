'''
  _   _                     _                 
 | | | | _____      __   __| | ___   ___  ___ 
 | |_| |/ _ \ \ /\ / /  / _` |/ _ \ / _ \/ __|
 |  _  | (_) \ V  V /  | (_| | (_) |  __/\__ \
 |_| |_|\___/ \_/\_/    \__,_|\___/ \___||___/
                                             
  ____        _   _                                      _    ___ 
 |  _ \ _   _| |_| |__   ___  _ __   __      _____  _ __| | _|__ \
 | |_) | | | | __| '_ \ / _ \| '_ \  \ \ /\ / / _ \| '__| |/ / / /
 |  __/| |_| | |_| | | | (_) | | | |  \ V  V / (_) | |  |   < |_| 
 |_|    \__, |\__|_| |_|\___/|_| |_|   \_/\_/ \___/|_|  |_|\_\(_) 
        |___/                                                     

'''
## ============================================================================
## How does Python work?
## ============================================================================
##
## For our purposes, we can think of Python as a machine that "interprets" your
## commands to bytecode and executes them one-by-one. This
## machine/program/interpreter is located on your system and is called
## "python.exe" (presuming you have it installed). By executing these steps,
## you can conduct calculations, write files, and do any other number of
## activities within the standard library.
##
## Python Standard Library:
##     https://docs.python.org/3/library/
##
## If you want to do something, odds are the standard library does it already.
##
## ============================================================================
## How do I give Python commands?
## ============================================================================
##
## We are going to cover two mechanisms for giving Python commands in this
## presentation:
##     1) by Python source code files; and, 
##     2) by using the Read-Evaluate-Print Loop (commonly known as the REPL). 
##
## ============================================================================
## Python Source Files
## ============================================================================
##
## As you saw in the previous lesson, Python has the ability to execute the
## commands in files line-by-line. We did this by running the Python
## interpreter in PowerShell and passing it an "argument", which is a separate
## string of characters containing information that the interpreter uses for
## program execution. And example of an argument would be "script.py" argument
## below:
##
##    python script.py
##
## This "script.py" argument tells Python, "Hey! Start running the commands
## in this file!". It will start running the command and pulling in other .py
## files if requested by your program.
##
## These .py source code files are basically just UTF-8 encoded text files.
## There's no special need to use anything to create them. They're just text
## containing Python commands. You use one or more of these .py files to
## create your first true program in the next section.
##
## ============================================================================
## Read-Eval-Print Loop (REPL)
## ============================================================================
##
## See also:
##     https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop
##
## In addition to using source code files, we can also use Python
## interactively by typing in commands one-by-one. This is useful for
## experimentation and debugging purposes. You can start the terminal in
## REPL/interactive mode by running Python without any arguments:
##
##    python
##
## This tells Python, "Hey, Python! I want you to read my commands as I
## type them one-by-one and then process the commands I give you." Open your
## command line and type:
##
##    python
##
## You should then get something that looks like this:
##
##    Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) ... on win32
##    Type "help", "copyright", "credits" or "license" for more information.
##    >>> 
##
##
## In IDLE, we use our "Shell" window.
##
## Try typing the following lines, pressing enter after each line:

'''

x = 'Now go away or I shall '
y = 'taunt you a second time.'
z = x + y
print(z)

'''

## If everything goes according to plan, your interpreter should print both
## of the above strings as a single sentence. If you get an error, try again.
## If you get a '...', Python thinks you're going to supply it with more info
## like a brace or a quote. If it gets too confusing just press CTRL + C or
## restart the shell, which will end the current command.
##
## Feel free to tinker with the REPL as we go through the presentation!
##
## Note 1: if you want to combine the two approaches, first running your 
## script and second dropping to the REPL, you can use an additional "-i"
## argument ("i" stands for interactive) in your command like this:
##
##     python -i script.py
##
## Note 2: Python was named after the comedy group "Monty Python's Flying
## Circus". You will see a lot of references to that group.
##
## Note 3: In IDLE, Alt + P goes to the previous REPL command and ALT + N
## goes to the next REPL command in the history.
##
## ============================================================================
## What does Python do after it starts the command?
## ============================================================================
##
## After you press enter, the Python interpreter performs a number of steps we
## needn't concern ourselves with like compilation and spinning up a Python-
## specific virtual machine.
##
## For our purposes, we can simply say that the Python interpreter will go
## to each commands, execute them, and then conduct whatever associated
## processes are required (such as reading text from the keyboard or waiting
## for files to load). Then interpreter will then exit itself (either by
## closing the window, by exiting back to the command line interface, or simply
## waiting for a new command in IDLE).
##
## ============================================================================
## Questions?
## ============================================================================
##
## On to _3_how_do_i_code.py ...
##
