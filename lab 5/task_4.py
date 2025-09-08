def calculate_score(applicant):
    """
    Calculate the score of a job applicant based on input features.

    Parameters:
    applicant (dict): A dictionary containing the applicant's details.

    Returns:
    int: The total score of the applicant.
    """
    score = 0

    # Education scoring
    education = applicant.get("education", "").lower()
    if education == "phd":
        score += 30
    elif education == "masters":
        score += 20
    elif education == "bachelors":
        score += 10
    else:
        score += 0  # No points for less than a bachelor's degree

    # Experience scoring
    experience = applicant.get("experience", 0)
    if experience >= 10:
        score += 30
    elif experience >= 5:
        score += 20
    elif experience >= 2:
        score += 10
    else:
        score += 0  # No points for less than 2 years of experience

    # Age scoring
    age = applicant.get("age", 0)
    if 25 <= age <= 40:
        score += 20  # Ideal working age range
    elif 18 <= age < 25 or 41 <= age <= 50:
        score += 10
    else:
        score += 0  # No points for age outside the range

    # Gender scoring (neutral)
    gender = applicant.get("gender", "").lower()
    if gender in ["male", "female", "non-binary"]:
        score += 10  # Equal points for all genders
    else:
        score += 0  # No points for unspecified gender

    return score


def main():
    """
    Main function to evaluate job applicants and calculate their scores.
    """
    print("Enter applicant details to calculate their score.")
    name = input("Enter the applicant's name: ")
    education = input("Enter the applicant's highest education (PhD, Masters, Bachelors, etc.): ")
    experience = int(input("Enter the applicant's years of experience: "))
    gender = input("Enter the applicant's gender (Male, Female, Non-binary, etc.): ")
    age = int(input("Enter the applicant's age: "))

    # Create an applicant dictionary
    applicant = {
        "name": name,
        "education": education,
        "experience": experience,
        "gender": gender,
        "age": age,
    }

    # Calculate the score
    score = calculate_score(applicant)
    print(f"Applicant: {applicant['name']}, Score: {score}")


if __name__ == "__main__":
    main()