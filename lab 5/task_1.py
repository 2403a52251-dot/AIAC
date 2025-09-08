import bcrypt
def register_user(users_db):
    """Register a new user with a username and hashed password."""
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists. Please try again.")
        return
    password = input("Enter a password: ").encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    users_db[username] = hashed_password
    print("User registered successfully!")

def login_user(users_db):
    """Login an existing user by verifying the hashed password."""
    username = input("Enter your username: ")
    password = input("Enter your password: ").encode('utf-8')
    if username in users_db and bcrypt.checkpw(password, users_db[username]):
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password. Please try again.")

def main():
    """Main function to handle the login system."""
    users_db = {}  # Dictionary to store username and hashed password
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_user(users_db)
        elif choice == "2":
            login_user(users_db)
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()