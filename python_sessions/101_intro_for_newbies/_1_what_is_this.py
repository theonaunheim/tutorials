'''
 __        ___           _     _       _   _     _    ___ 
 \ \      / / |__   __ _| |_  (_)___  | |_| |__ (_)__|__ \
  \ \ /\ / /| '_ \ / _` | __| | / __| | __| '_ \| / __|/ /
   \ V  V / | | | | (_| | |_  | \__ \ | |_| | | | \__ \_| 
    \_/\_/  |_| |_|\__,_|\__| |_|___/  \__|_| |_|_|___(_) 

'''
## ============================================================================
## Introduction
## ============================================================================
##
## Welcome to the Python Intro For Newbies! (Tested on Python 3.7.0)
##
## Presenter:
##     Theo Naunheim <theonaunheim@gmail.com>
##
## Audience:
##     People who are new to the Python language and coding in general.
##
## Goals:
##
##     1) to provide a simplified overview of the Python language to
##     non-developers;
##
##     2) give you the knowledge you need to start tinkering around in Python;
##     and start creating your own code;
##
##     3) give you some pointers on where you can go to continue;
##
##     4) answer any questions you may have about Python; and,
##
##      5) ¯\_(ツ)_/¯
##
## ============================================================================
## What is Python?
## ============================================================================
##
## Wiki Link:
##     https://en.wikipedia.org/wiki/Python_(programming_language)
##
## Python is a general purpose programming language that is notable for its
## flexibility, clarity, and ease of use. It was created in the early 1990s by
## the Dutch computer scientist Guido von Rossum, and has become more and more
## popular ever since.
##
## Because of its clarity and simplicity, it is often one of the first
## languages taught to new programmers. This has led to its widespread adoption
## in a variety of sectors, especially web programming and data science.
##
## ============================================================================
## What is going on here? What is all this red and green stuff?
## ============================================================================
##
## You are actually inside of a Python file that you've opened in IDLE, which
## is Python's default editor. You can tell its a Python file because it's a
## text file that ends with the '.py' suffix and because ... I'm telling you
## it's a Python file and I'm totally a trustworthy person. More to the point--
## we're doing this because if you code Python, you're going to be reading,
## writing, and running these files.
##
## We are going to use this editor and Python interpreter (a.k.a. "shell") to
## conduct the vast majority of this presentation. You can think of the editor
## as something that saves simple text data to a file (without all the confusing
## formatting junk you see from most word processors). You can just as easily
## use Notepad for your editor and trigger the Python shell via the command
## 'python' in PowerShell or CMD.exe.
##
## Side note: we will refer to these Python files as scripts, code, module or 
## source code. For the time being, you can just presume these concepts are the
## same.
##
## So what is all this red and green stuff? The answer is that these are
## 'comments'. They are statements that convey information to you--the person
## reading the code--but that Python will ignore. Most of this presentation is
## comments.
##
## See "An Informal Introduction to Python" for additional detail:
##     https://docs.python.org/3.6/tutorial/introduction.html

'''

Multi-line comments (like this one) are denoted with triple single quotes.

'''

"""

Alternatively: 
    They can be denoted with triple double quotes like this.

"""

# Here are some single line comments.
# Note the hash/octothorpe that starts the comments.
# Don't take my word for it, though.
# Try executing this file with python.exe!
# Python will read it line-by-line and execute your commands in sequence.

## ============================================================================
## Test
## ============================================================================

print("Everything before this was skipped over without doing anything.")
print("Because comments.")
print("Now I am executing code, though.") # Now back to comments.

## The proper way to run this source file would be to open up a command line
## like PowerShell and then type Python and then the path to your file (note:
## you should not type a hash mark):
##
##     python ~/Desktop/101_intro_for_newbies/_1_what_is_this.py
##
## Your output would then be:
##
## Everything before this was skipped over without doing anything.
## Because comments.
## Now I am executing code, though. 
##
## If the above did not work, odds are something on your system is not set up
## correct. This could be because you have not already installed Python or
## possible because you ran the script from the wrong directory.
##
## We are going to be lazy, however. We are simply going to copy all the Python
## commands we want to run and paste them in the 'scratch' window. Then you can
## simply go to the "Run" menu and select "Run Module". I am even lazier than
## that, however, and I will simply be pressing F5.
##
## Our output will then show in the "Shell" window.
##
## ============================================================================
## Any questions before we get started in earnest?
## ============================================================================
##
## If not, go to the "File" menu and select the next module.
##
## On to _2_what_is_python.py ...
## 
