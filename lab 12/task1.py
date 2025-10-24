def linear_search(lst, value):
    """
    Searches for 'value' in 'lst' and returns its index if found. 
    Returns -1 if the value is not in the list.
    """
    for idx, item in enumerate(lst):
        if item == value:
            return idx
    return -1

# Example usage
if __name__ == "__main__":
    test_list = [1, 3, 5, 7, 9, 11, 13]
    search_value = 7
    
    print(f"Searching for {search_value} in {test_list}")
    result = linear_search(test_list, search_value)
    
    if result != -1:
        print(f"Found {search_value} at index {result}")
    else:
        print(f"{search_value} not found in the list")
    
    # Test with value not in list
    search_value2 = 4
    result2 = linear_search(test_list, search_value2)
    print(f"Searching for {search_value2}: {'Found at index ' + str(result2) if result2 != -1 else 'Not found'}")