#file appended defined here
first = ""
#file with the additions to be made
second = ""
fob = open(second).readlines()

with open(second, 'a') as file:
    for i in fob:
        file.write (i)
     
print ("operation completed")
