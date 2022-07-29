#This is an exercise in control flows, aka the ifs, elses, and fors!

if True:
    print("This statement is true!")

if 1==2:
    print("This if statement is true!")
else:
    print("This if statement is false!")

#Practicing else ifs

temp= 25

if temp>30:
    print("It is too hot")
elif temp> 15:
    print("Just right")
elif temp>0:
    print("It is too cold")
else:
    print("It is probably snowing")

#Critical to note is that the else ifs will run until the FIRST one is satisfied.

#Onto for loops. We can make these pretty terse.

for x in [1,2,3,4,5]:
    print("x is", x)

#Notice that we couldn't use the typical listing index method [1:6]
#It is because we have a different way of pulling that. It is range()

for number in range(10):
    print(number ** 2)

#A personal note. saving and compiling causes the program to open itself up again. So it might be worthwhile to compile and then save? Sounds risky

print("This sentence was before we saved")

#The mystery continues. Perhaps Le chen might know the solution. If not, stackexchange it is.

#An exercise that checks to find things in our lists
#Find the days of the week that contain the letter e in them using a for loop

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

for x in range(7):
    if "e" in days[x]:
        print(days[x])

#Pretty slick, no? 

