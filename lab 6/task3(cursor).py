# The Age class represents a person's age and provides methods to convert years to days, weeks, and months,
# as well as to classify the age group.
class Age:
    def __init__(self, years):
        # Initialize the Age object with the number of years
        self.years = years

    def to_days(self):
        # Convert years to days (assuming 1 year = 365 days)
        return self.years * 365

    def to_weeks(self):
        # Convert years to weeks (assuming 1 year = 52 weeks)
        return self.years * 52

    def to_months(self):
        # Convert years to months (assuming 1 year = 12 months)
        return self.years * 12

    def classify_age_group(self):
        # Classify the age group based on the number of years
        if self.years < 0:
            return "Invalid age"
        elif self.years <= 12:
            return "Child"
        elif self.years <= 19:
            return "Teen"
        elif self.years <= 59:
            return "Adult"
        else:
            return "Senior"

# Create an Age object for a person who is 25 years old
person_age = Age(25)
# Print the age in days
print("Age in days:", person_age.to_days())
# Print the age in weeks
print("Age in weeks:", person_age.to_weeks())
# Print the age in months
print("Age in months:", person_age.to_months())
# Print the age group classification
print("Age group:", person_age.classify_age_group())

