'''
   _       _
  (_)_ __ | |_ _ __ ___
  | | '_ \| __| '__/ _ \
  | | | | | |_| | | (_) |
  |_|_| |_|\__|_|  \___/

'''
##=============================================================================
## Welcome to Python 101 For Devs
##=============================================================================
## Feel free to message me or ask questions as we go through this presentation.
##
## Before we start: we will be doing the majority of this inside of IDLE,
## which is Python's default (but woefully underpowered) text editor. This is
## intended to be an interactive session in which you execute commands and ask
## questions as we go along. If you followed in instructions in the !README.txt
## file, you should be good to go. If not, feel free to just follow along.
##
## We are going to be doing this presentation inside of Python source files
## like this one. Mainly because if you're going to code Python, you're going
## to spend a ton of time reading, writing, and executing these files.
##
##=============================================================================
## What is Python?
##=============================================================================
##
## https://www.python.org
## https://docs.python.org/3/tutorial/
## https://docs.python.org/3/
##
## Python is a high-level, general purpose programming language that focuses on
## clarity, flexibility, and ease of use. Python is an interpreted language,
## meaning that instead of compiling software, we use an interpreter to run our
## programs.
##
##=============================================================================
## Why do we care?
##=============================================================================
##
## The language is becoming increasingly popular in the financial services
## space because of its use in data science and web programming. Due to its
## simplicity, it is also often one of the first programming languages taught
## in computer science programs (giving it a wide user base). It also lets you
## get things done comparatively quickly, which makes it an attractive language
## for adminstrators and analysts of all stripes.
##
##=============================================================================
## So what is the plan?
##=============================================================================
##
## We are going to go through a series of lessons and examples to demonstrate
## Python's abilities and teach you how to use it. If you have questions, stop
## me. That's what I'm here for. Questions are appreciated; stupid questions
## doublly so. If you have a stupid questions, it's because I'm doing my job
## wrong.
##
##=============================================================================
## Housekeeping
##=============================================================================
##
## So first off ... you'll notice that we are inside of Python sources files,
## which are just UTF-8 text files with a '.py' prefix. For the purposes of
## this presentation, you will follow along with the content in your editor
## window. When we want to execute Python statements, we will either trigger
## them in PowerShell or simply copy the code your want to run to the
## "scratch.py" window and them execute via F5 or the "Run Menu".
##
## Note: any line that starts with a hash ('#') is a comment that will not
## be executed. Similarly, the triple single quote (''') or triple double quote
## (""") denote multiline comments.

"""Long comment is
        loooooooooooooooong...
"""

## Try running the command below from your "scratch" window to check that
## everything works:

import random

scifi_heroines = ['Alyx Vance', 'Katniss Everdeen', 'Ellen Ripley']
choice = random.choice(scifi_heroines)

print(f'My favorite scifi heroine is {choice}!')

## Finally, stop me at any point if you think there's something I could
## expound and/or improve upon. Any feedback is appreciated.
##
##=============================================================================
## WARNING!!! WARNING!!! WARNING!!
##=============================================================================
##
## As developers, it is incumbant upon you to obey your respective development
## and model risk management policies of your respective organizations.
##
##=============================================================================
## Questions?
##=============================================================================

