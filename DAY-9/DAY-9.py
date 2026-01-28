## control flows and loop logic

#if-elif-else:

age = (int(input("what is your age :\n")))

if age >= 18:
    print("you are an adult\n")
elif age >= 13:
    print("you are a teenager\n")
else:
    print("you are a child\n")

#nested if and using if with input :

score = int(input("enter your score :"))
if score  >= 50 :
    print("pass")
    if score  >= 90 :
        print("grade A")
    elif score >= 75:
        print("grade b")
    else :
        print("grade c")
else :
    print("fail")

##short hand if expressions :

x = 10
if x > 5 : print ("greater than 5 ")

#ternary operator 

age = 17 
message = "adult" if age >= 18 else "minor"
print(message)

# combining with logical operator:

age = 19
country = "USA"

if age >= 19 and country == "USA":
    print("eligibile to vote in USA")


# boolean short circuiting 

##explain with "and":
##
#if x > 0 and y / x > 2 


# Multiple Conditions & Precedence

age = 20 
is_student = True 
if age >= 18 and is_student:
    print("eligible for student discount")

##not operator :
is_admin = False

if not is_admin:
    print("access denied")

## real life example 
username_correct = True
password_correct = False 
is_admin = True

if(username_correct and password_correct) or is_admin:
    print("access granted")

# comparative chains
age = int(input("whats your age?\n"))
if 18 <= age <= 70:
    print("you are a fucker\n")

# nested if logic and decision trees 

hungry = True
want_pizza = False

if hungry:
    print("You're hungry!")
    if want_pizza:
        print("Ordering pizza...")
    else:
        print("Ordering something else...")
else:
    print("Not hungry.")

# logic in python :

apply = True
income = int(input("whats your income :"))
credit_score = int(input("whats your credit score :"))

if apply:
    if income > 300000:
        if credit_score > 700:
            print("approved")
        else:
            print("rejected : poor credit score")
    else:
        print("rejected : poor income")
else:
    print("not applied")

    ## while loops 

    i = 10 
    while i >= 1:
        print(i)
        i -= 1

# using while for user input 

password = ""
while password != "python" :
    password = input("enter password :")
print("access granted")

# infinite while loops 
#while True:
   # print("running,,,,,")


# break in python - stop the looop forcefully 

while True:
    cmd = input("Enter command:")

    if cmd == "exit":
        break

    print("you typed:", cmd)


# continue - to skip the next iteration 
i = 1
while i <= 10:
    i+=1
    if i%2 == 0:
        continue 
    print(i)
    exit()


# counting with conditions 
###example : sum of numbers 1-100

i = 1
total = 0 

while i <=  100:
    total += i 
    i+=1 
print("sun : ", total)


#Nested while loops 

row = 1 
while row <= 3:
    col = 1 
    while col<=4:
        print(col,end=" ")
        col+=1 
    print()
    row+=1

#else with while loop
i = 1
while i<=5:
    print(i)
    i+=1
else:
    print("loop completed")

#example :

while True:
    print("1. Add")
    print("2.Delete")
    print("3.Exit")

    choice = input("enter your choice : \n")
    
    if choice == "1":
        print("adding items")
    elif choice == "2":
        print("deleting items...")
    elif choice == "3":
        print("goodbye!")
        break
    else:
        print("invalid choice ")
        exit()

# while loop for validation

age = int(input("whats your age?" ))
while age <= 0:
    print("invalid age:")
age = int(input("enter age again : \n"))

#Using while to simulate processes
battery = 100
while battery > 0:
    print("Using battery:", battery)
    battery -= 15

print("Battery dead.")



