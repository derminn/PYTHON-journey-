##diving deeper into lists 

### LOOPING THROUGH LISTS 

#using for loop
fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
 print(fruit)


#using range index 

name = ["dermin", "derminotsocool", "derminiscool"]

for i in range(len(fruits)):
   print(i, fruits[i])




#using while loop

numbers = [10, 20, 30, 40]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

#using enumerate()

name = ["dermin", "derminotsocool", "derminiscool"]

for index, name in enumerate(name,start=1):
   print(index,name)
 

# list comprehension 

squares = [x*x for x in [1,2,3,4]]
print(squares) #[1, 4, 9, 16]


## NESTED LISTS 
nested = [[1,2,3], [4,5,6]]

#nested[0] → [1,2,3]

#nested[1] → [4,5,6]


#accessing values inside nested lists 

print(nested[1][2]) 

#nested[1]-->second list-->[4,5,6]
#[2]-->value at index 2 --> 6

##output = 6

#looping through nested lists 

students = [
    ["Alice", 85, 92],
    ["Bob", 78, 88],
    ["Charlie", 95, 89]
]

for i, student in enumerate(students):
   print(f"student {i+1}:")  
   for j, value in enumerate(student):
      if j == 0:
         print(f" name:{value}")
      else: print(f" score:{j}: {value}")
      print() 

# examples:
sales_data = [
   [100,200,300],
   [150,250,350],
   [175,275,375]
]

for i, week in enumerate(sales_data):
   total=sum(week)
   print(f"Week {i+1} total : ${total}")
for day in range(len(sales_data[0])):
   total = sum(week[day] for week in sales_data)
   print(f"Day {day+1} total : ${total}")



## nested list comprehension 

matrix = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]

flat = [value for row in matrix for value in row]
print(flat)

#transforming while flattening:

squares = [num*num for row in matrix for num in row]
print(squares)

#creating a 2D list :

multiplied = [[num * 10 for num in row] for row in matrix]
print(multiplied)

#transposing a matrix 
matrix = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]

transpose = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]
print(transpose)

#irregular nested lists 

weird = [[1,2,3], [4],[5,6,7,8,9]]
