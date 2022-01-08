#!/usr/bin/env python3

import random
import colorama

colorama.init()


def get_greeting(person):
    """ Get a random greeting, greeting *person* """
    greetings = ["hello!", "hi", "namaste", "privet", "konichiwa", "nihao!"]
    return f"{random.choice(greetings).title()}, {person}."


def color_greeting(color, person):
    """ Colorise the greeting """
    if not color in ("red", "green", "yellow", "blue", "magenta", "cyan"):
        raise ValueError("Color %s is not supported" % color)
    coloured_greeting = eval(
            f"colorama.Fore.{color.upper()} + '{get_greeting(person)}'"
                )
    colorama.Style.RESET_ALL
    return coloured_greeting

def main():
    """ Main Function """
    person = "Mikhail"
    color = ("cyan", "magenta", "blue", "red")[random.randint(0, 4)]
    print(color_greeting(color, person))

main()


