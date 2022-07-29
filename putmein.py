#An exploration of inputs. Will code a MUD
import sys

name = input("What is your name?")

if len(name) < 5:
    print("Your parents couldn't afford more letters for a name?")
elif 5< len(name) < 10:
    print("Boring")
else:
    print("More letters than the inches your mom takes from me")

age = input("What is your age?")

age = int(age)

if age < 18:
    print("This program wasn't meant for you")
    sys.exit()
else: 
    print("Cool")

sex = input("Sex?")

if (sex == "Yes please!"):
    print("You sly dog")
else:
    print("Seems like someone isn't getting some")

