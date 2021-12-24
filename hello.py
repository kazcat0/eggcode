#!/usr/bin/env python3

import datetime
import random
random.seed()

def divider():
    print("")

def prompt_choice(choices):
    print("Pick an option from the following menu:")
    for letter in choices:
        desc = choices.get(letter)
        print(f"{letter} - {desc}")
    while True:
        try:
            selection = input("Your choice: ").strip()
            if selection in choices:
                return selection
            else:
                print("Invalid choice, please try again.")
        except EOFError:
            return None
        except KeyboardInterrupt:
            return None

class Egg:
    def __init__(self):
        self.height = 0 # meters
        self.weight = 0 # kilograms
        self.birthdate = 0 # time?
        self.moisture = 0 #dryness to wetness
        self.telepathy = 0 #egg chattiness
    
    def __repr__(self):
        return f"Egg(height = {self.height} meters, weight = {self.weight}kg, birthdate = {self.birthdate}, moisture = {self.moisture})"

METERS = 1
KILOGRAMS = 1
CENTIMETERS = 0.01
GRAMS = 0.001

def random_percent(min, max):
    half = (max / 2) * 0.01
    percent = (random.randint(0, 10) * 0.01)
    return 1.00 - half + percent

def birth_egg():
    egg = Egg()
    egg.birthdate = datetime.datetime.now()
    print("You wake up. It is noon. Saturday. 3pm.")
    print("You get up and hit the showers.")
    print("On the way, you trip and stumble over an egg.")
    print("You don't remember there being an egg.")
    print("How do you think it got here?")
    divider()
    options = {
            "1": "You laid it, as one does",
            "2": "It broke in to your house",
            "3": "You were sciencing too hard",
    }
    choice = prompt_choice(options)
    divider()
    if choice == "1":
        egg.height = 5 * CENTIMETERS
        egg.weight = 100 * GRAMS
        egg.moisture  = "dry"
        print("That's right, you laid a small egg last night.")
    elif choice == "2":
        egg.height = 1 * METERS
        egg.weight = 50 * KILOGRAMS
        egg.moisture  = "average"
        print("You see the door has been kicked in. Uh-oh.")
    elif choice == "3":
        egg.height = 30 * CENTIMETERS
        egg.weight = 2 * KILOGRAMS
        egg.moisture  = "wet"
        print("You scienced up a ruler-sized egg.")
    egg.height *= random_percent(0, 10)
    egg.weight *= random_percent(0, 10)
    return egg

def look_egg(egg):
    print(f"Your egg is: {egg}")

def main():
    print("Welcome to eggcode!")
    divider()
    egg = birth_egg()
    look_egg(egg)

if __name__ == "__main__":
    main()
