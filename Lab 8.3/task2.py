def assign_grade(score):
    """
    Assigns a grade based on the score.
    Handles boundary and invalid inputs.
    
    Args:
        score: The score to evaluate (can be string, int, or float)
        
    Returns:
        str: Grade letter (A, B, C, D, F) or error message
    """
    # Step 1: Convert input to float and handle non-numeric inputs
    try:
        score = float(score)  # Convert string/int to float for consistent comparison
    except (ValueError, TypeError):
        # Handle cases like "abc", "", None, or other non-convertible inputs
        return "Invalid input: not a number"

    # Step 2: Validate score range (0-100)
    if score < 0 or score > 100:
        # Handle negative scores or scores above 100
        return "Invalid input: score must be between 0 and 100"

    # Step 3: Assign grade based on score ranges
    # Using if-elif chain for grade assignment
    if score >= 90:        # 90-100: Excellent
        return "A"
    elif score >= 80:     # 80-89: Good  
        return "B"
    elif score >= 70:     # 70-79: Satisfactory
        return "C"
    elif score >= 60:     # 60-69: Passing
        return "D"
    else:                 # 0-59: Failing
        return "F"

# Example usage: Interactive program
user_input = input("Enter the score: ")  # Get user input as string
grade = assign_grade(user_input)          # Call function with user input
print(f"Grade: {grade}")                  # Display the result


