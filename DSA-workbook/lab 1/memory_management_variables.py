a = 2
b = 2
print(id(a)) #1632496144
print(id(b)) #1632496144

'''In python variables work like tags. When you do an assignment in Python, it tags
the value with the variable name. Other languages have 'variables',Python has 'names'.'''

a += 1
print(id(a)) #1632496160 now points to 3 which exists at other memory location
print(id(b)) #1632496144

#in C language variables are considered as a box of storage , but in python everything is an object
#if we assign a=2 there will be 2 in memory and a just points to it , then when we assign b=2 b also points to 2 instead of creating another box of memory like in C