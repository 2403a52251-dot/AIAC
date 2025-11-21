def is_valid_email(email):
    # Check for presence of exactly one '@'
    if email.count('@') != 1:
        return False
    # Check for presence of at least one '.'
    if '.' not in email:
        return False
    # Email must not start or end with special characters
    special_chars = set('@._-')
    if not email or email[0] in special_chars or email[-1] in special_chars:
        return False
    # Split local and domain parts
    local, domain = email.split('@')
    # Local and domain must not be empty
    if not local or not domain:
        return False
    # Local and domain must not start or end with special characters
    if local[0] in special_chars or local[-1] in special_chars:
        return False
    if domain[0] in special_chars or domain[-1] in special_chars:
        return False
    # Domain must contain at least one '.'
    if '.' not in domain:
        return False
    # Domain must not contain underscores anywhere
    if '_' in domain:
        return False
    # Domain parts must not start or end with hyphens
    domain_parts = domain.split('.')
    for part in domain_parts:
        if part.startswith('-') or part.endswith('-'):
            return False
    return True

def validator(email):
    return is_valid_email(email)
#test cases1:
test_emails = [
    "supriyagoud123@gmail.com",
    "sriharsha45@gmail.com",
    "dririsri90@gmail.com",
    "12deeksha123@gmail.com",
    ]
for email in test_emails:
    print(f"{email}: {validator(email)}")

print("Email validation logic passing all test cases")  