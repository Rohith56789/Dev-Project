#creating string
str1 = "hello "
str2 = "world"
str3 ='''
    This is my
    multi line string
    '''
#string concatenation
greeting = str1 + " " + str2
print(greeting)
print(str3) #multi line string

print(f"{str1} {str2}") #f string
 #repeat string
print((str1+ "")* 3) #repeat string

 #Acessing string characters
print(str1[0])
print(str1[-1])

 #slicing string
print(str1[0:3]) #hello