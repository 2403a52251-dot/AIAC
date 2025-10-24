"""
Simple Linear Programming Solution
Chocolate Manufacturing Company Case Study
"""

# Problem: Maximize profit from Chocolate A and B
# Constraints: Milk <= 5, Choco <= 12
# Profit: A = Rs 6, B = Rs 5

print("Chocolate Manufacturing Optimization")
print("=" * 40)

# Find optimal solution using grid search
max_profit = 0
best_x = 0
best_y = 0

print("Checking all possible combinations:")
print("A\tB\tMilk\tChoco\tProfit")
print("-" * 35)

for x in range(6):  # Units of A (0 to 5)
    for y in range(6):  # Units of B (0 to 5)
        milk_used = x + y
        choco_used = 3*x + 2*y
        profit = 6*x + 5*y
        
        # Check if solution is feasible
        if milk_used <= 5 and choco_used <= 12:
            print(f"{x}\t{y}\t{milk_used}\t{choco_used}\t{profit}")
            
            # Update best solution
            if profit > max_profit:
                max_profit = profit
                best_x = x
                best_y = y

print("\n" + "=" * 40)
print("OPTIMAL SOLUTION:")
print(f"Produce {best_x} units of A and {best_y} units of B")
print(f"Maximum Profit: Rs {max_profit}")
print(f"Milk used: {best_x + best_y}/5")
print(f"Choco used: {3*best_x + 2*best_y}/12")