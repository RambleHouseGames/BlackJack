from MainMenuState import MainMenuState

CurrentState = MainMenuState()

while not CurrentState.GameIsOver:
    CurrentState = CurrentState.Update()