class age:
    def __init__(self, years):
        self.years = years

    def to_days(self):
        return self.years * 365

    def to_weeks(self):
        return self.years * 52

    def to_months(self):
        return self.years * 12

    def classify_age_group(self):
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

if __name__ == "__main__":
    person_age = age(25)
    print("Age in days:", person_age.to_days())
    print("Age in weeks:", person_age.to_weeks())
    print("Age in months:", person_age.to_months())
    print("Age group:", person_age.classify_age_group())
