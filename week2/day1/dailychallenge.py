name= input ("give me a string with 10 characters  ")
number= len(name)
if number > 10:
    print("string too long ")
elif number <10:
    print("string not long enough")
elif number == 10:
    print( name[0])
    print( name[9])

print( name[0]) 
print( name[0:1]) 
print( name[0:2]) 
print( name[0:3]) 
print( name[0:4]) 
print( name[0:5]) 
print( name[0:6]) 
print( name[0:7]) 
print( name[0:8]) 
print( name[0:9]) 