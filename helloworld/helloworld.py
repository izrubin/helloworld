import random
import datetime

def helloworld(name=None, nextm=None, roll=None):
    """
    return hello world, or hello {name}
    """

    # print greeting
    if not name:
        print("Hello, world!")
    else:
        print("Hello, {}.".format(name))

    # print days until the next millenium
    if nextm:
        nday = datetime.datetime(3000, 1, 1)
        diff = nday - datetime.datetime.now()
        print("There are {} days until the new millenium.".format(diff.days))

    # print the numbers you would get from rolling two 6-sided dice
    if roll:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print("You rolled a {} and a {}.".format(die1, die2))
        