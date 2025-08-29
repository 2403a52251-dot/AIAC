def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            # Avoid division by zero
            if values[j] != 0:
                ratio = values[i] / values[j]
                results.append((i, j, ratio))
            else:
                results.append((i, j, "undefined"))
    return results

# Test with the given numbers
nums = [5, 10, 15, 20, 25]
print("Computing ratios for:", nums)
print("Results (index1, index2, ratio):")
ratios = compute_ratios(nums)
for result in ratios:
    print(f"  {result}")

# Additional test with zero to demonstrate error handling
print("\nTesting with zero in the list:")
nums_with_zero = [5, 0, 15, 20]
print("Computing ratios for:", nums_with_zero)
ratios_with_zero = compute_ratios(nums_with_zero)
for result in ratios_with_zero:
    print(f"  {result}")
