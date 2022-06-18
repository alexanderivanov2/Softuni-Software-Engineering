from tic_tac_toe.setup import setup
from tic_tac_toe.play_engine import play

if __name__ == "__main__":
    setup()
    play()
    new_game = input("Do you want to play a new game? y/n: ")
    while new_game == "y":
        setup()
        play()
        new_game = input("Do you want to play a new game? y/n: ")
    print("Bye!")
