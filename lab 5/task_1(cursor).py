import bcrypt
import json
import os
import getpass
import re
from datetime import datetime

class LoginSystem:
    def __init__(self, data_file="users.json"):
        """Initialize the login system with data persistence."""
        self.data_file = data_file
        self.users_db = self.load_users()
        self.current_user = None
        self.session_start = None
    
    def load_users(self):
        """Load users from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return {}
        return {}
    
    def save_users(self):
        """Save users to JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.users_db, f, indent=2)
        except Exception as e:
            print(f"Error saving users: {e}")
    
    def validate_password(self, password):
        """Validate password strength."""
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        if not re.search(r"[A-Z]", password):
            return False, "Password must contain at least one uppercase letter"
        if not re.search(r"[a-z]", password):
            return False, "Password must contain at least one lowercase letter"
        if not re.search(r"\d", password):
            return False, "Password must contain at least one digit"
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False, "Password must contain at least one special character"
        return True, "Password is valid"
    
    def register_user(self):
        """Register a new user with validation."""
        print("\n=== USER REGISTRATION ===")
        username = input("Enter a username: ").strip()
        
        if not username:
            print("Username cannot be empty!")
            return False
        
        if username in self.users_db:
            print("Username already exists. Please try again.")
            return False
        
        # Get password securely
        while True:
            password = getpass.getpass("Enter a password: ")
            is_valid, message = self.validate_password(password)
            if is_valid:
                break
            else:
                print(f"Password validation failed: {message}")
                retry = input("Try again? (y/n): ").lower()
                if retry != 'y':
                    return False
        
        # Confirm password
        confirm_password = getpass.getpass("Confirm password: ")
        if password != confirm_password:
            print("Passwords do not match!")
            return False
        
        # Hash password and store
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.users_db[username] = {
            'password': hashed_password.decode('utf-8'),
            'created_at': datetime.now().isoformat(),
            'last_login': None
        }
        self.save_users()
        print("User registered successfully!")
        return True
    
    def login_user(self):
        """Login an existing user."""
        print("\n=== USER LOGIN ===")
        username = input("Enter your username: ").strip()
        password = getpass.getpass("Enter your password: ")
        
        if username not in self.users_db:
            print("Invalid username or password.")
            return False
        
        stored_data = self.users_db[username]
        stored_password = stored_data['password'].encode('utf-8')
        
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            self.current_user = username
            self.session_start = datetime.now()
            # Update last login time
            self.users_db[username]['last_login'] = datetime.now().isoformat()
            self.save_users()
            print(f"Login successful! Welcome, {username}")
            return True
        else:
            print("Invalid username or password.")
            return False
    
    def logout_user(self):
        """Logout current user."""
        if self.current_user:
            session_duration = datetime.now() - self.session_start if self.session_start else None
            print(f"Goodbye, {self.current_user}!")
            if session_duration:
                print(f"Session duration: {session_duration}")
            self.current_user = None
            self.session_start = None
        else:
            print("No user is currently logged in.")
    
    def view_users(self):
        """View all registered users (admin function)."""
        if not self.current_user:
            print("Please login first to view users.")
            return
        
        print("\n=== REGISTERED USERS ===")
        if not self.users_db:
            print("No users registered.")
            return
        
        for username, data in self.users_db.items():
            created = data.get('created_at', 'Unknown')
            last_login = data.get('last_login', 'Never')
            print(f"Username: {username}")
            print(f"  Created: {created}")
            print(f"  Last Login: {last_login}")
            print("-" * 30)
    
    def delete_user(self):
        """Delete a user account."""
        if not self.current_user:
            print("Please login first.")
            return
        
        print("\n=== DELETE USER ACCOUNT ===")
        username = input("Enter username to delete: ").strip()
        
        if username not in self.users_db:
            print("User not found.")
            return
        
        if username == self.current_user:
            confirm = input("Are you sure you want to delete your own account? (yes/no): ").lower()
            if confirm == 'yes':
                del self.users_db[username]
                self.save_users()
                print("Account deleted successfully.")
                self.logout_user()
            else:
                print("Account deletion cancelled.")
        else:
            print("You can only delete your own account.")
    
    def change_password(self):
        """Change password for current user."""
        if not self.current_user:
            print("Please login first.")
            return
        
        print("\n=== CHANGE PASSWORD ===")
        current_password = getpass.getpass("Enter current password: ")
        
        # Verify current password
        stored_data = self.users_db[self.current_user]
        stored_password = stored_data['password'].encode('utf-8')
        
        if not bcrypt.checkpw(current_password.encode('utf-8'), stored_password):
            print("Current password is incorrect.")
            return
        
        # Get new password
        while True:
            new_password = getpass.getpass("Enter new password: ")
            is_valid, message = self.validate_password(new_password)
            if is_valid:
                break
            else:
                print(f"Password validation failed: {message}")
                retry = input("Try again? (y/n): ").lower()
                if retry != 'y':
                    return
        
        # Confirm new password
        confirm_password = getpass.getpass("Confirm new password: ")
        if new_password != confirm_password:
            print("Passwords do not match!")
            return
        
        # Update password
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        self.users_db[self.current_user]['password'] = hashed_password.decode('utf-8')
        self.save_users()
        print("Password changed successfully!")
    
    def show_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("           LOGIN SYSTEM")
        print("="*50)
        
        if self.current_user:
            print(f"Logged in as: {self.current_user}")
            print("\n1. Logout")
            print("2. Change Password")
            print("3. View Users")
            print("4. Delete Account")
            print("5. Exit")
        else:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")
    
    def run(self):
        """Main function to run the login system."""
        print("Welcome to the Login System!")
        
        while True:
            self.show_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if self.current_user:  # User is logged in
                if choice == "1":
                    self.logout_user()
                elif choice == "2":
                    self.change_password()
                elif choice == "3":
                    self.view_users()
                elif choice == "4":
                    self.delete_user()
                elif choice == "5":
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:  # User is not logged in
                if choice == "1":
                    self.register_user()
                elif choice == "2":
                    self.login_user()
                elif choice == "3":
                    print("Exiting the system. Goodbye!")
                    break
                else:-
                    print("Invalid choice. Please try again.")

def main():
    """Initialize and run the login system."""
    try:
        login_system = LoginSystem()
        login_system.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
