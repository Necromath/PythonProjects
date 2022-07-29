#Welcome to the dictionary tab :) 
#Dictionary are fancy, unordered lists with convenient ways to reference them

#Here is an example of a dictionary

organisation = {"name": "Disney",
                "founded": 1923
                }

#As an aside. There are 3 brackets we use in python.
#Round brackets (), are used for math, functions, and methods
#Square brackets [], are used for lists, and "getting things" from our lists and dictionaries.
#Curly brackets {}, are used for creating dictionaries and creating sets. 

print(organisation)

print(organisation['name'])

print(organisation['founded'])

print("Disney was founded in the year" , organisation['founded'], "by Walt Disney")

#Commas let us separate what we're printing on the same line. Allowing us to combine strings with ints and floats 

#We can add more key/value pairs into a dictionary in the following way

organisation['headquarters'] = "Orlando"

print(organisation['headquarters'])

organisation["numbers"] = [1,2,3]

#You can chain lists inside dictionaries like a total badass

print(organisation["numbers"][2])

#That should print 3

#You can also append to the list!

organisation["numbers"].append(15)

print(organisation["numbers"])


