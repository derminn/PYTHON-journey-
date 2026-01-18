#Escape Sequences in Strings

print('EVERY ONE IS BRAINDED\n') # line break
print('Days\tTopics\tExercises')
print('Day 1\t4\t3')
print('Day 2\t5\t2')
print('Day 3\t3\t6')
print('Day 4\t8\t8')
print('This is a backslash  symbol (\\)') # To write a backslash


#String formating

##Old Style String Formating (% Operator)

### strings only
name_1 = "dermicool"
name_2 = "derminotsocool"

name = "dermin has two nicknames , which are %s and %s" %(name_1 ,name_2)

print(name)

### strings and numbers 

radius =float(input("enter the number : \n", ))

pi = 3.14

area = pi * radius**2

formated_string = "the area of the cirlce with radius  %d is %.2f." %(radius ,area)

print(formated_string)


## new style string formatting (introduced in python version 3)

first_name = "dermin"
last_name = "otsocool"

full_name = "the one learning pyhon is {}{}".format(first_name,last_name)

print(full_name)

a = 15
b = 25

print("{} + {} = {}".format(a ,b , a+b))

##String Interpolation / f-Strings (Python 3.6+)

a = 15
b = 25

print(f"{a} + {b} = {a + b}")


## string slicing 

s = "hello python"

print(s[0:5]) #output : hello 

print(s[6:]) #output : python

print(s[9:]) #last 3 words 

print(s[::-1]) #reversing the string 


language = "python"
print(language[0::2])
print(language[2:6:2])
print(language[1:6:5])
print(language[2:6:3])


####STRING METHODS

s = "dermin is not so cool"
print(s.capitalize()) # Dermin is not so cool
print(s.count("o"))  # 4
print(s.endswith('ol')) #true 

w = "dermin\t is\t very\t uncool"
print(w.expandtabs()) #dermin   is      very    uncool
print(w.expandtabs(20)) #dermin               is                  very                uncool

d = "derminotsocool"
print(d.find("o")) #6
 
print(d.rfind("o")) #12

first_name = "dermi"
last_name = "notsocool"
age = 15

s = "my name is {}{} and i am {} years old.".format(first_name,last_name,age)

print(s)

radius = float(input("enter the radius :"))
pi = 3.14
area = pi*radius**2
result = "the area of the circle with radius {} is {}".format(str(radius), str(area))
print(area)

#isal() (checks alpha numeric character )

x = "threemonkeys"
print(x.isalnum()) #true

x = "three monkeys"
print(x.isalnum()) #false space is not alpha numeric 

x = "3monkeys"
print(x.isalnum()) #true 

#isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)

senpai = "derminiscool"
print(senpai.isalpha()) #true 

senpai = "dermin is cool"
print(senpai.isalpha())  #false : space again excluded 

##isdecimal()

s = "three monkeys"
print(s.isdecimal()) #false : space not alowwed 

w = "12515"
print(w.isdecimal()) #true 


#isdigit()

monkeys = "three"
print(monkeys.isdigit()) #false 

monkeys = "3" 
print(monkeys.isdigit()) #true 


#isnumeric()

num = "10"
print(num.isnumreric()) #true 

num = "/u00BD"
print(num.isnumeric()) #true 

num = "10.5"
print(num.isnumeric()) #false 


#isidentifier()

s = "3lilmonkeys"
print(s.isidentifier()) #false : it starts with number 

s = "three_lil_monkeys"
print(s.isidentifier()) #true 

#islower 

s = "three lil momkeys"
print(s.islower()) #true 

s = "Three lil momkeys"
print(s.islower()) #false 

#is upper 

s = "three lil momkeys"
print(s.isupper()) #false 

s = "Three lil momkeys"
print(s.isupper()) #true


#join()

web_tech = ["HRML", "CSS" , "JAVA" ]
result = "#" .join(web_tech)
print(result)

#strip()
s = "three monkeys"
print(s.strip("tys"))


#replace()

s = "thre little monkeys"
print(s.replace("monkeys", "dermin"))

#title()

s = "three lil  monkeys"
print(s.title())

#swapcase()

s = "three lil  monkeys" 
print(s.swapcase()) #THREE LIL MONKEYS 

#startswith():checks if the string starts with specified string 