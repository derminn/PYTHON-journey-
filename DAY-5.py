
#bitwise AND (&=)

x = 6 # Binary: 110
y = 3 # Binary: 011
result = x & y 
print(result) # OUTPUT = 2 (Binary : 010)

#Bitwise OR:

x = 6   # Binary: 110
y = 3   # Binary: 011

# Apply Bitwise OR
result = x | y

# Print the result
print(result)  # Output: 7 (Binary: 111)


#Bitwise NOT

x = 5    # Binary:  0000 0101

# Apply Bitwise NOT
result = ~x    # Result: -6

# Print the result
print(result)   # Output: -6


# BITWISE XOR : -

x = 6   # Binary: 110
y = 3   # Binary: 011

# Apply Bitwise XOR
result = x ^ y

# Print the result
print(result)  # Output: 5 (Binary: 101)

##  Bitwitse RIGHT shift Operator

x = 16  # Binary: 10000

# Shift bits right by 2
result = x >> 2

print(result)  # Output: 4 (Binary: 0100)

##  Bitwise LEFT  Shift Operator

x = 4   # Binary: 0100

# Shift bits left by 2
result = x << 2

print(result)  # Output: 16 (Binary: 10000)

### COOMPARISION OPERATORS :
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)


### LOGICAL OPERATORS :
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False