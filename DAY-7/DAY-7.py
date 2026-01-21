#####LISTS#####

#syntax

lst = list()
empty_list = list() #this is an empty list 
print(len(empty_list)) #0

##using square brackets 
lst = [] #this is also an empty list 

#basic examples 

fruits = ["banana", "orange" ,"lemon"]
vegetables = ["tomato" , "potato" , "cabbage" , "onion"]

print("fruits :",fruits )
print("number of fruits : ",len(fruits))

print("vegetables : ",vegetables)
print("number of vegetables : ",len(vegetables))

#different datatypes in a list 

lst = ["dermicool",2555 , True , {"country" : "india" , "city" : "amd"}]


#accessing items in list using positive indexing 

names = ["dermin" , "dermicoool" , "derminotsocool"]
og_name = names[0]
print(og_name) #dermin

#accessing items in list using negative indexing 

names = ["dermin" , "dermicoool" , "derminotsocool"]
og_name = names[-3]
print(og_name) #dermin 

#unpacking of list
lst = ["dermin","dermicool","derminotsocool"]
x,y,z = lst 

print(x)

#examples 

first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]

print(rest)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

#slicing items from list 

##positive indexing
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[0:4]
print(all_fruits)

orange_and_mango = fruits[1:3]
print(orange_and_mango)

##negative indexing 
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[-4:]
print(all_fruits)

orange_and_mango = fruits[-3:-1]
print(orange_and_mango)

#modifying lists 

fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "avocado"
print(fruits)

fruits[1] = "apple"
print(fruits)

     


#Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

#adding items to list 

names = ["dermin", "dermicool" ,"derminotsocool"]
names.append("derminiscool")
print(names) #['dermin', 'dermicool', 'derminotsocool', 'derminiscool']

#inserting items into list 

names = ["dermin", "dermicool" ,"derminotsocool"]
names.insert(1,"derminiscool")
print(names)  #['dermin', 'dermicool', 'derminotsocool', 'derminiscool']

#removing items from list 

names = ["dermin", "dermicool" ,"derminotsocool"]
names.remove("dermin")
print(names) #['dermicool', 'derminotsocool']

#removing items using pop 

names = ["dermin", "derminisnotsocool", "deermicool", "derminnnnn"]
names.pop()
print(names) #['dermin', 'derminisnotsocool', 'deermicool']

names.pop(0)
print(names) #['derminisnotsocool', 'deermicool']

names.pop(1)
print(names)

#removing items using del 

names = ["dermin", "derminisnotsocool", "deermicool", "derminnnnn"]
#del names #this would delete the entire list
#print(names) #this would give "NameError: name 'names' is not defined"

del names[0] #this would remove the "derminnn",as it is at the 0th position according to the +ve indexing.

#copying a list 

list = ["dermin", "dermicool"]
list_copy = list.copy()

print(list_copy)

#joining a list 
##USING + OPERATOR 

positive_numbers = [1,2,3,4,5,6,7,8,9]
zero = [0]
negative_numbers = [-1,-2,-3,-4,-5,-6,-7,-8,-9]

integers = negative_numbers + zero + positive_numbers
print(integers)

##using extend method 
num1 = [1,2,3,4,5]
num2 = [7,9,0,8]

num1.extend(num2)
print("Number:\n",num1)

#counting items in the list 
names = ["dermin", "derminisnotsocool", "deermicool", "derminnnnn"]
print(names.count("dermin")) #1

even_numbers = [2,2,2,2,4,4,4,4,4]
print(even_numbers.count("2"))

#finding index of an item 
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1

#reversing a list 
fruits = ['banana', 'orange', 'mango', 'lemon'] #['lemon', 'mango', 'orange', 'banana']

fruits.reverse()

# sorting list items 
names = ["dermin", "derminotsocool", "derminiscool"]
names.sort() #ascending 
names.sort(reverse=true) #descending
print(names) #strings would be arranged in alphabetical order

###sorted()
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))     # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']

