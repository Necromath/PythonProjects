#If you want to make a new file in python. What you need to do is type, touch [filename].py and then summon the file with nvim [filename]* 
print("This is my first sentence!")

#This is my first comment. Welcome, Mauricio! This is our first serious journey into python as an Academic. :) Keep it up. Will probably make a new folder for the python stuff though. 
#There are several types of variables in Python. Strings, Int, Floats, Boolean. THESE DO NOT INTERACT WITH EACH OTHER. So Don't try to. There are ways to convert them, but that is for later.
print(type(2))
print(type(2.0))
print(type("Here are some words!"))
print(type(3.4 ** 2.0))

# Notice that the only way to really see ANYTHING in python requires us to use the print statement. Very important!

# Setting variables is easy, just type in what you want something to be.
box = "3 Dimensional"
print(box)
print(type(box))

#box = 4 
#The line above is commented to demonstrate how we play with the if else statements work.
#NOTICE: all the if else statements use a colon to indicate stuff. MAKE SURE YOU DO NOT LOSE SIGHT OF THESE.

if type(box) == str:
    print("Box is a string")
else:
    print("Box is not a string")

print("Here is an example of a boolean:")
print (" Is 2 < 1 ?")
print (2<1)

#We also have the and v. or statements. Just like logic. Or needs one to be true. And needs both.

#This marks the end of the first python program :)
