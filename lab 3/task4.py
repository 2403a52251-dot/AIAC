from typing import Dict
USERS: Dict[str, str] = {}

def register_user(username: str, password: str) -> bool:
	"""Register a user with a plain in-memory store. Returns False if taken."""
	if not username or not password:
		raise ValueError("Username and password must be non-empty")
	if username in USERS:
		return False
	USERS[username] = password
	return True


def login_user(username: str, password: str) -> bool:
	"""Check credentials against the in-memory store."""
	if not username or not password:
		return False
	stored = USERS.get(username)
	return stored == password


if __name__ == "__main__":
	while True:
		print("1) Register\n2) Login\n0) Exit")
		choice = input("Choose (1/2/0): ").strip().lower()
		if choice == "1":
			u = input("New username: ").strip()
			p = input("New password: ")
			try:
				ok = register_user(u, p)
				print("Registered" if ok else "Username already exists")
			except ValueError as exc:
				print(f"Error: {exc}")
		elif choice == "2":
			u = input("Username: ").strip()
			p = input("Password: ")
			print("Login successful" if login_user(u, p) else "Invalid credentials")
		elif choice in ("0", "q", "quit", "exit"):
			print("Goodbye!")
			break
		else:
			print("Invalid choice")


