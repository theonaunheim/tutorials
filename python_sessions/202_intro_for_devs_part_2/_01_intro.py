'''
 _       _             
(_)_ __ | |_ _ __ ___  
| | '_ \| __| '__/ _ \ 
| | | | | |_| | | (_) |
|_|_| |_|\__|_|  \___/ 
                       

'''
##=============================================================================
## Generally
##=============================================================================
##
## This presentation is a continuation of what we covered in our previous
## presentation, Python 201 for Devs, Part 1. Previously we built a base of
## general knowledge around Python grammar. Here, we arere going to look at
## some of the more complex concepts you will need to build out more 
## significant programs.
##
## Same as before, this presentation is going to be conducted from within IDLE,
## which is Python's text editor. It is not feature-rich, but it is installed
## by default with Python (which is why we are using it).
##
## The links you see are worth taking a look at. Many of them cover these
## topics better than I can. The first of these I would point you to is the
## official Python 3 tutorial:
##
## https://docs.python.org/3/tutorial/
##
## As a reminder, you will want to put the code we are going over on the left
## side of your screen. Then put the "Shell" window in the top right hand
## corner, and open the "scratch" file and put it in the lower right hand
## corner. Then to make sure everything is working, copy paste this in the
## "scratch" window and run it (either via the Run Menu, or F5).

import random

scifi_heroines = ['Alyx Vance', 'Katniss Everdeen', 'Ellen Ripley']
choice = random.choice(scifi_heroines)

print(f'My favorite scifi heroine is {choice}!')

## If it does not work, something has gone horribly, horribly wrong.
##
## Stop me if you have questions. Especially for stupid questions. If
## you have a question, odds are others do too. Stop me if you have suggestions
## for how to improve things. Without feedback I am flying blind.
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
