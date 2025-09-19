from task3 import is_sentence_palindrome

# Test cases: (sentence, expected_result)
test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("12321", True),
    ("", True),
    ("No lemon, no melon", True),
    ("Madam, I'm Adam", True),
    ("Was it a car or a cat I saw?", True),
    ("Eva, can I see bees in a cave?", True),
    ("Never odd or even", True),
    ("Hello, World!", False),
    ("Red roses run no risk, sir, on Nurse's order.", True),
    ("Step on no pets", True),
    ("Not a palindrome", False),
    ("Able was I, I saw Elba", True),
    ("Go hang a salami, I'm a lasagna hog.", True),
]

passed = 0
for i, (sentence, expected) in enumerate(test_cases, 1):
    result = is_sentence_palindrome(sentence)
    status = "PASS" if result == expected else "FAIL"
    print(f"Test {i:2}: {sentence!r:40} | Expected: {expected!s:5} | Got: {result!s:5} | {status}")
    if status == "PASS":
        passed += 1

print(f"\nTotal: {len(test_cases)}, Passed: {passed}, Failed: {len(test_cases) - passed}")
if passed == len(test_cases):
    print("okay all correct")
else:
    print("Some tests failed!")