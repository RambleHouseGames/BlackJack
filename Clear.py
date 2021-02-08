# Clears the screen so that the game board can be redrawn
# I have a Mac so the Windows Version is untested but I think system('cls') is right

from os import system, name 

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac
    else: 
        _ = system('clear') 