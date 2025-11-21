def run_shopping_cart_tests_verbose():
    from task4 import ShoppingCart

    cart = ShoppingCart()
    total = 0
    passed = 0

    print("Test 1: Add item to empty cart")
    cart.add_item("apple", 2.5)
    total += 1
    result = "PASS" if cart.items == {"apple": {"price": 2.5, "quantity": 1}} else "FAIL"
    print(f"  Expected: {{'apple': {{'price': 2.5, 'quantity': 1}}}}")
    print(f"  Got:      {cart.items}")
    print(f"  Result:   {result}\n")
    if result == "PASS":
        passed += 1

    print("Test 2: Add same item again (should increment quantity)")
    cart.add_item("apple", 2.5)
    total += 1
    result = "PASS" if cart.items["apple"]["quantity"] == 2 else "FAIL"
    print(f"  Expected quantity: 2")
    print(f"  Got:               {cart.items['apple']['quantity']}")
    print(f"  Result:            {result}\n")
    if result == "PASS":
        passed += 1

    print("Test 3: Add different item")
    cart.add_item("banana", 1.0)
    total += 1
    expected = {"apple": {"price": 2.5, "quantity": 2}, "banana": {"price": 1.0, "quantity": 1}}
    result = "PASS" if cart.items == expected else "FAIL"
    print(f"  Expected: {expected}")
    print(f"  Got:      {cart.items}")
    print(f"  Result:   {result}\n")
    if result == "PASS":
        passed += 1

    print("Test 4: Remove one quantity of apple")
    cart.remove_item("apple")
    total += 1
    result = "PASS" if cart.items["apple"]["quantity"] == 1 else "FAIL"
    print(f"  Expected apple quantity: 1")
    print(f"  Got:                     {cart.items['apple']['quantity']}")
    print(f"  Result:                  {result}\n")
    if result == "PASS":
        passed += 1

    print("Test 5: Remove last quantity of apple (should remove item)")
    cart.remove_item("apple")
    total += 1
    result = "PASS" if "apple" not in cart.items else "FAIL"
    print(f"  Expected: apple not in cart")
    print(f"  Got:      {'apple' in cart.items}")
    print(f"  Result:   {result}\n")
    if result == "PASS":
        passed += 1

    print("Test 6: Remove item not in cart (should do nothing)")
    before = dict(cart.items)
    cart.remove_item("orange")
    total += 1
    result = "PASS" if cart.items == before else "FAIL"
    print(f"  Expected: {before}")
    print(f"  Got:      {cart.items}")
    print(f"  Result:   {result}\n")
    if result == "PASS":
        passed += 1

    print("Test 7: Total cost calculation")
    cart.add_item("orange", 3.0)
    cart.add_item("banana", 1.0)
    # Now: banana x2, orange x1
    total += 1
    expected_cost = 2 * 1.0 + 3.0
    actual_cost = cart.total_cost()
    result = "PASS" if abs(actual_cost - expected_cost) < 1e-8 else "FAIL"
    print(f"  Expected cost: {expected_cost}")
    print(f"  Got:           {actual_cost}")
    print(f"  Result:        {result}\n")
    if result == "PASS":
        passed += 1

    print("Test 8: Add item with float price")
    cart.add_item("milk", 2.75)
    total += 1
    result = "PASS" if "milk" in cart.items and abs(cart.items["milk"]["price"] - 2.75) < 1e-8 else "FAIL"
    print(f"  Expected: milk in cart with price 2.75")
    print(f"  Got:      {cart.items.get('milk', None)}")
    print(f"  Result:   {result}\n")
    if result == "PASS":
        passed += 1

    print("Test 9: Remove all items and check total cost is zero")
    cart.remove_item("banana")
    cart.remove_item("banana")
    cart.remove_item("orange")
    cart.remove_item("milk")
    total += 1
    result = "PASS" if cart.total_cost() == 0 else "FAIL"
    print(f"  Expected cost: 0")
    print(f"  Got:           {cart.total_cost()}")
    print(f"  Result:        {result}\n")
    if result == "PASS":
        passed += 1

    print("Test 10: Add multiple items and check total cost")
    cart.add_item("bread", 1.5)
    cart.add_item("eggs", 2.0)
    cart.add_item("bread", 1.5)
    total += 1
    expected_cost = 2 * 1.5 + 2.0
    actual_cost = cart.total_cost()
    result = "PASS" if abs(actual_cost - expected_cost) < 1e-8 else "FAIL"
    print(f"  Expected cost: {expected_cost}")
    print(f"  Got:           {actual_cost}")
    print(f"  Result:        {result}\n")
    if result == "PASS":
        passed += 1

    print(f"Total: {total}, Passed: {passed}, Failed: {total - passed}")
    if passed == total:
        print("okay all correct")
    else:
        print("some tests failed")

print("\n--- Verbose ShoppingCart Test Cases ---\n")
run_shopping_cart_tests_verbose()
