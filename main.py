from game_data import data
from art import logo, vs
import random


def pickRandom():

    item = random.choice(data)

    return item


def show(a, b):

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print()
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    print()


def getPop(a, b):

    if a['follower_count'] >= b['follower_count']:
        return 'a'

    else:
        return 'b'


def game():

    a = {}
    b = pickRandom()
    score = 0
    print(logo)

    while True:

        a = b
        b = pickRandom()

        show(a, b)

        ch = input("Who has more followers? Type 'A' or 'B': ").lower()

        if ch == getPop(a, b):
            score += 1

            print(f"You're right! Current score: {score}")

        else:

            print(f"Sorry, that's wrong. Final score: {score}")
            break


game()
