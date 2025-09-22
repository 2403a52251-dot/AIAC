#refractor the code below withCleaner logic using elif or dictionary mapping
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# print the grade of 5 students with scores 95, 85, 75, 65, 55
print(grade(95))
print(grade(85))
print(grade(75))
print(grade(65))
print(grade(55))
