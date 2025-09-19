# Short test cases for is_valid_email function
from task1 import is_valid_email

# Test cases: (email, expected_result)
test_cases = [
    # Valid emails
    ("user@example.com", True),
    ("user.name@example.com", True),
    ("user_name@example.com", True),
    ("user-name@example.com", True),
    ("a@b.co", True),
    ("user@domain.co.uk", True),
    
    # Invalid emails
    ("plainaddress", False),           # No @
    ("user@example", False),           # No dot
    ("", False),                       # Empty
    ("@example.com", False),           # Missing local
    ("user@", False),                  # Missing domain
    (".user@example.com", False),      # Starts with dot
    ("user@example.com.", False),      # Ends with dot
    ("user@domain_.com", False),       # Underscore in domain
    ("user@domain-.com", False),       # Domain ends with hyphen
    ("user@-domain.com", False),       # Domain starts with hyphen
]

# Run tests
passed = 0
for email, expected in test_cases:
    result = is_valid_email(email)
    status = "PASS" if result == expected else "FAIL"
    print(f"{email:<25} {expected!s:<5} {result!s:<5} {status}")
    if result == expected:
        passed += 1

print(f"\nTotal: {len(test_cases)}, Passed: {passed}, Failed: {len(test_cases)-passed}")
print(" All tests passed!" if passed == len(test_cases) else " Some tests failed!")