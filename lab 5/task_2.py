def loan_approval(name, income, credit_score):
    """Evaluate loan approval based on income and credit score."""
    print(f"Evaluating loan approval for {name}...")
    
    # Basic criteria for loan approval
    if income >= 50000 and credit_score >= 700:
        print(f"Loan approved for {name}!")
        return True
    else:
        print(f"Loan denied for {name}.")
        return False

def main():
    """Main function to test loan approval for different names."""
    applicants = [
        {"name": "John", "income": 60000, "credit_score": 750},
        {"name": "Priya", "income": 45000, "credit_score": 720},
        {"name": "Ahmed", "income": 55000, "credit_score": 680},
        {"name": "Maria", "income": 70000, "credit_score": 800},
    ]
    
    for applicant in applicants:
        loan_approval(applicant["name"], applicant["income"], applicant["credit_score"])

if __name__ == "__main__":
    main()