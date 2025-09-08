def greet_user(name, gender):
    """
    Greet the user with an appropriate title based on their gender.

    Parameters:
    name (str): The name of the user.
    gender (str): The gender of the user (e.g., Male, Female, Non-binary).

    Returns:
    str: A greeting message.
    """
    # Determine the title based on gender
    if gender.lower() == "male":
        title = "Mr."
    elif gender.lower() == "female":
        title = "Ms."
    elif gender.lower() == "non-binary":
        title = "Mx."
    else:
        title = ""  # No title for unspecified or other genders

    # Return the greeting message
    return f"Hello, {title} {name}! Welcome."

# Example usage
if __name__ == "__main__":
    name = input("Enter your name: ")
    gender = input("Enter your gender (Male, Female, Non-binary, etc.): ")
    print(greet_user(name, gender))