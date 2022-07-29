#This is where we learn about FUNCTIONS
#These are the basis for everything ... 
# A function is a variable with code inside of it. So you call the function (variable) and it executes the code inside of it. 
#They are like recipes, waiting to be executed.
#Functions are introduced with the command def [function] () :

def cake():
    print("Yum. Cake.")

cake()


#Functions take inputs, called arguments.

def cake(slices):
    print("I have", slices, "slices of cake!")

cake(slices=8)

box = cake(slices=15)

#print(box) 

#So what happened here? print box isn't working. Why?
#It is because... print is just for show and tell!
#print says show me box, don't give me what is inside.
#To obtain the output from a function. You have to use return!

def cake(slices):
    return print("I have", slices, "slices of cake!")

box = cake(slices= 50)

#------------------------------

#Trickier one

def add(x,y):
    return x + y

print(add(x=5,y=3))

p = add(x=3,y=5)
q = add(x=p, y=5)

print(p,q)

#Area of a circle

pi = 3.14

def circarea(radius):
    return pi*(radius**2)

answer = circarea(radius=5)

print(answer)

#Investment formula

def invest(principal, rate, time):
    return principal*((1+rate)**time)

investment = invest(10000, .01, 10)

print(investment)
