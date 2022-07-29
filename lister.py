#This is where I will practice with lists!
#Lists are made with square brackets! They are their own type too!

days = ["Monday", "Tuesday", "Wednesday", "Thursday" , "Friday", "Saturday", "Sunday"]

print(type(days))
print(days)

#These lists are indexed with a start at 0, keep that in mind.

print(days[5])

#Funny enough though, negative indices are accepted in these lists.
#Just keep in mind that theyll go backwards on the list too!

#Lists can also be 'sliced' in such a way.

print(days[1:3])

#The notation for this stuff is like a half open interval. This is [1,3), so just 1 and 2
#A colon, : , indicated what side of the half open interval you are on. And it terminates on the next modulo 0
# So for example, print(days[:-1]) says: print the days list until position -1, which is Sunday. So we get Mon-Sat.

print(days[:-1])

#We update lists with the .append() command. 

brothers = ["Mario", "Luigi"]

print(brothers)

brothers.append("Wario")

print(brothers)

#----------------------------------#
