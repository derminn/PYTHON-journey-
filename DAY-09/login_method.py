
correct_username = "dermicool"
correct_password = "Dermin@2411"

attempts = 0

while attempts < 3:
    username = input("enter username: \n")
    password = input("enter password : \n")
    
    if username == correct_username and password == correct_password:
        print("login successful!")
        break 
    else:
        attempts += 1 
        print(f"incorrect info ! attempts left: {3-attempts}")
if attempts == 3:
    print("account blocked.")
  
