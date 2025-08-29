def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            if values[j] != 0:  # Avoid division by zero
                ratio = values[i] / values[j]
                results.append((i, j, ratio))
            else:
                results.append((i, j, None))  # Append None if division by zero
    return results

# Example usage
nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))
