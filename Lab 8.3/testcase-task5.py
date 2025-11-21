from task5 import convert_date_format

test_cases = [
    # (input, expected_output)
    ("2023-07-15", "15-07-2023"),      # normal date
    ("2000-01-01", "01-01-2000"),      # start of century
    ("1999-12-31", "31-12-1999"),      # end of year
    ("2020-02-29", "29-02-2020"),      # leap day
    ("2021-11-09", "09-11-2021"),      # single digit day/month
    ("0001-01-01", "01-01-0001"),      # earliest possible year
    ("2022-10-05", "05-10-2022"),      # random date
    ("1980-06-30", "30-06-1980"),      # another random date
    ("2010-09-08", "08-09-2010"),      # another random date
    ("2024-12-31", "31-12-2024"),      # future date
    # Invalid cases
    ("2023/07/15", ValueError),        # wrong separator
    ("2023-7-15", "15-7-2023"),        # single digit month (should work)
    ("2023-07-32", "32-07-2023"),      # invalid day, but function doesn't validate
    ("", ValueError),                  # empty string
    ("2023-07", ValueError),           # missing day
    ("2023-07-15-01", ValueError),     # too many parts
]

passed = 0
total = 0

for i, (input_val, expected) in enumerate(test_cases, 1):
    total += 1
    try:
        result = convert_date_format(input_val)
        if isinstance(expected, type) and issubclass(expected, Exception):
            print(f"Test {i}: Input={input_val!r} | Expected Exception {expected.__name__} | Got={result!r} | FAIL")
        elif result == expected:
            print(f"Test {i}: Input={input_val!r} | Expected={expected!r} | Got={result!r} | PASS")
            passed += 1
        else:
            print(f"Test {i}: Input={input_val!r} | Expected={expected!r} | Got={result!r} | FAIL")
    except Exception as e:
        if isinstance(expected, type) and isinstance(e, expected):
            print(f"Test {i}: Input={input_val!r} | Expected Exception {expected.__name__} | Got Exception {type(e).__name__} | PASS")
            passed += 1
        else:
            print(f"Test {i}: Input={input_val!r} | Expected={expected!r} | Got Exception {type(e).__name__}: {e} | FAIL")

print(f"\nTotal: {total}, Passed: {passed}, Failed: {total - passed}")
if passed == total:
    print("okay all correct")
else:
    print("some tests failed")
