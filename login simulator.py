def login():
    
    credentials = {"username1": "password123"}
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    
    if username in credentials and credentials[username] == password:
        print(f"Welcome, {username}! Login successful.")
    else:
        print(f"Login failed. Incorrect username or password.")

login()
