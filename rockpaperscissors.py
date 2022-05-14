import random
import datetime



def rock_paper_scissors(func):
    def wrapper(*args, **kwargs):
        options= ["rock", "paper", "scissors"]
        my_time= datetime.date.today()
        print(options) 
        print(my_time) 
        play= random.choice(options)
        print("THE COMPUTER CHOSE:  " + play)
        func(*args, **kwargs)
        if play == "rock" and hand == "paper"\
            or play == "paper" and hand == "scissors"\
            or play == "scissors" and hand == "rock":
            print("YOU WON")
        elif play == hand:
            print("YOU TIE")
        else:
            print("YOU LOST")
    return wrapper

hand= str(input("CHOSE BETWEN ROCK; PAPER; SCISSOR; AND WRITE IT: "))
@rock_paper_scissors
def my_turn():
    print("I PICKED:  " + hand)

if __name__ == "__main__":
    my_turn()