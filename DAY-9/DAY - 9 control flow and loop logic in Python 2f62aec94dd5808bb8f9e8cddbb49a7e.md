# DAY - 9 : control flow and loop logic in Python

# *Conditional Statements (if-elif-else):*

BASIC IF-ELIF :

Conditional statements allow your program to execute different code blocks based on conditions.

```python
age = int(input("what is your age :\n"))

if age >= 18:
    print("you are an adult\n")
elif age >= 13:
    print("you are a teenager\n")
else:
    print("you are a child\n")
```

- `if` checks the first condition
- `elif` (else if) checks additional conditions if previous ones are False
- `else` executes when all conditions are False
- Conditions are evaluated **top to bottom**, stopping at the first True condition

---

# *Nested Conditionals:*

A **nested if** is simply:

> An if statement inside another if statement.
> 

This allows the program to make **multi-level decisions**, similar to asking follow-up questions.

EXAMPLE :

```python
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
```

## Decision Trees :

A **Decision Tree** is what nested logic looks like visually.

```python
          hungry?
             |
      ┌──────┴──────┐
     Yes            No
     |               |
 want pizza?      Not hungry
     |
  ┌──┴──┐
 Yes    No
 |      |
Pizza  Something else
```

This helps us plan logical paths clearly.

## More Complex Example  :

```python
is_registered = True
password_correct = True
two_factor_enabled = True
two_factor_verified = False

if is_registered:
    print("User found")
    if password_correct:
        print("Password OK")
        if two_factor_enabled:
            if two_factor_verified:
                print("Login success!")
            else:
                print("Verify 2FA to continue")
        else:
            print("Login success (no 2FA)")
    else:
        print("Wrong password")
else:
    print("User does not exist")
```

This is how **real authentication systems** work.

## Summary :

| Concept | Meaning |
| --- | --- |
| Nested If | If inside another If |
| Used for | Multi-step decisions |
| Looks like | A decision tree |
| Pros | More control |
| Cons | Can get messy |
| Fix | Use logical operators / early exit |

---

# *Shorthand If Expressions:*

single line if statement.

```python
x = 10
if x > 5: print("greater than 5")
```

Ternary operator :

```python
age = 17 
message = "adult" if age >= 18 else "minor"
print(message)
```

- Ternary operator: `value_if_true if condition else value_if_false`
- More concise for simple conditional assignments
- Improves code readability for basic conditions

---

# *Boolean short - circuiting :*

**Boolean short-circuiting** is when Python **stops evaluating a logical expression as soon as the final result is known**.

This happens with the operators:

- `and`
- `or`

### **1. For `and`**

Rule: **If the first value is False**, no need to check the second — result will be False.

Example:

```python
Falseandprint("Hello")
```

- `False` is enough to know the answer
- `print("Hello")` never runs!

---

### **2. For `or`**

Rule: **If the first value is True**, no need to check the second — result will be True.

Example:

```python
Trueorprint("Hello")
```

- `True` is enough to know the answer
- `print("Hello")` never runs!

# **Truth Table Explanation:**

| Operator | Stops when | Example |
| --- | --- | --- |
| `and` | first is **False** | `False and X` |
| `or` | first is **True** | `True or X` |

---

# *WHILE LOOPS:*

A **while loop** repeats as long as a **condition is True**.

```python
while condition:
    do something

```

Example:

```python
i = 1
while i <= 5:
print(i)
i += 1
```

## Using while for user input:

Very useful when repeating until correct data is entered:

```python
password = ""
while password != "python":
    password = input("Enter password: ")

print("Access granted!")
```

## `break` — stop the loop forcefully:

```python
while True:
    cmd = input("Enter command: ")
    if cmd == "exit":
        break
    print("You typed:", cmd)

```

break exits immediately.

## `continue` — skip to next iteration:

```python
i = 1
while i <= 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
#this prints only odd numbers.
```

## Counting with conditions:

Example: sum of numbers 1–100.

```python
i = 1
total = 0

while i <= 100:
    total += i
    i += 1

print("Sum =", total)
```

## While loop vs For loop:

| Feature | while | for |
| --- | --- | --- |
| Based on | condition | sequence |
| Use when | no known length | known length |
| Risk | infinite loops | low |

## Nested while loops:

Example printing a grid:

```python
row = 1
while row <= 3:
    col = 1
    while col <= 4:
        print(col, end=" ")
        col += 1
    print()
    row += 1

```

output :

```python
1 2 3 4
1 2 3 4
1 2 3 4
```

## `else` with while loop :

`else` executes when the loop finishes normally.
 
Example:

```python
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Finished looping!")
```

If loop ends by `break`, else doesn’t run.

## While loop for validation:

```python
age = int(input("Enter age: "))
while age <= 0:
    print("Invalid age!")
    age = int(input("Enter age again: "))

```

## Using while to simulate processes:

```python
battery = 100
while battery > 0:
    print("Using battery:", battery)
    battery -= 15

print("Battery dead.")

```