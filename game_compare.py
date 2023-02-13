"""A simple game that compares user input to a randomly-generated integer"""

import random

TARGET = [None]

def compare(user_input):
    if TARGET[0] is None:
        return "`Please start game by typing !startgame`\n"
    try:
        user_input = int(user_input)
        assert 0 <= user_input <= 100
    except:
        return (
            "`ValueError, try again..`\n"
            "`Please give a integer between 0 and 100 using the format !game[integer]..`\n"
            "`For eg: !game27`"
        )

    if user_input == TARGET[0]:
        TARGET[0] = None
        return ":partying_face::partying_face::partying_face:`Bingo! You found the number!`:partying_face::partying_face::partying_face:"
    elif user_input <= TARGET[0]:
        return "`Your answer is smaller than target!`"
    else:
        return "`Your answer is greater than target!`"


def reset(TARGET):
    TARGET[0] = random.randint(0,100)
    return

def start_game():
    reset(TARGET)
    return (
        "`Please give a integer between 0 and 100 using the format !game[integer]..`\n"
        "`For eg: !game27`"
    )