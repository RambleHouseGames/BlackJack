# Super Awesome Black Jack.
# By Quinn Larson
# Written for Oplus Code Challenge

from MainMenuState import MainMenuState

CurrentState = MainMenuState() # Start in MainMenuState

while not CurrentState.GameIsOver: # Main Loop
    CurrentState = CurrentState.Update() # Update The Current State which will give you the next one