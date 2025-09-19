from task2 import assign_grade

# Test cases: (input, expected_output)
test_cases = [
    (95, "A"),                # High A
    (90, "A"),                # Boundary A
    (89.9, "B"),              # Just below A
    (85, "B"),                # Middle B
    (80, "B"),                # Boundary B
    (75, "C"),                # Middle C
    (70, "C"),                # Boundary C
    (65, "D"),                # Middle D
    (60, "D"),                # Boundary D
    (59.9, "F"),              # Just below D
    (0, "F"),                 # Lowest valid score
    (100, "A"),               # Highest valid score
    (-5, "Invalid input: score must be between 0 and 100"),  # Negative score
    (105, "Invalid input: score must be between 0 and 100"), # Above 100
    ("abc", "Invalid input: not a number"),                  # Non-numeric input
    ("", "Invalid input: not a number"),                     # Empty string
    (None, "Invalid input: not a number"),                   # None input
]

passed = 0
for i, (input_value, expected) in enumerate(test_cases, 1):
    result = assign_grade(input_value)
    status = "PASS" if result == expected else "FAIL"
    print(f"Test {i:2}: Input={input_value!r:8} | Expected={expected!r:40} | Got={result!r:40} | {status}")
    if status == "PASS":
        passed += 1

print(f"\nTotal: {len(test_cases)}, Passed: {passed}, Failed: {len(test_cases) - passed}")
if passed == len(test_cases):
    print("okay all correct")
else:
    print("Some tests failed!")
