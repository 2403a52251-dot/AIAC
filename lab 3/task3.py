def calculate_power_bill(units_consumed, rate_per_unit=0.12, fixed_charge=50):
    """
    Calculate electricity power bill.
    
    Args:
        units_consumed (float): Number of electricity units consumed
        rate_per_unit (float): Rate per unit in currency (default: 0.12)
        fixed_charge (float): Fixed monthly charge (default: 50)
        
    Returns:
        dict: Bill breakdown including total amount
    """
    # Calculate energy charge
    energy_charge = units_consumed * rate_per_unit
    
    # Calculate total bill
    total_bill = energy_charge + fixed_charge
    
    # Calculate tax (assuming 5% tax)
    tax_rate = 0.05
    tax_amount = total_bill * tax_rate
    
    # Final amount including tax
    final_amount = total_bill + tax_amount
    
    return {
        'units_consumed': units_consumed,
        'rate_per_unit': rate_per_unit,
        'energy_charge': round(energy_charge, 2),
        'fixed_charge': fixed_charge,
        'subtotal': round(total_bill, 2),
        'tax_rate': f"{tax_rate * 100}%",
        'tax_amount': round(tax_amount, 2),
        'final_amount': round(final_amount, 2)
    }

def display_bill(bill_details):
    """Display the power bill in a formatted way."""
    print("=" * 40)
    print("           ELECTRICITY BILL")
    print("=" * 40)
    print(f"Units Consumed:        {bill_details['units_consumed']} kWh")
    print(f"Rate per Unit:         ${bill_details['rate_per_unit']}")
    print(f"Energy Charge:         ${bill_details['energy_charge']}")
    print(f"Fixed Charge:          ${bill_details['fixed_charge']}")
    print("-" * 40)
    print(f"Subtotal:              ${bill_details['subtotal']}")
    print(f"Tax ({bill_details['tax_rate']}):            ${bill_details['tax_amount']}")
    print("=" * 40)
    print(f"TOTAL AMOUNT:          ${bill_details['final_amount']}")
    print("=" * 40)

# Main program
if __name__ == "__main__":
    print("Power Bill Calculator")
    print("-" * 20)
    
    try:
        # Get user input
        units = float(input("Enter units consumed (kWh): "))
        
        if units < 0:
            print("Error: Units consumed cannot be negative!")
        else:
            # Calculate bill
            bill = calculate_power_bill(units)
            
            # Display bill
            display_bill(bill)
            
    except ValueError:
        print("Error: Please enter a valid number!")
    
    # Example calculations
    print("\n" + "=" * 50)
    print("Example Calculations:")
    print("=" * 50)
    
    example_units = [100, 250, 500, 1000]
    
    for units in example_units:
        bill = calculate_power_bill(units)
        print(f"\nFor {units} kWh consumption:")
        print(f"Total Bill: ${bill['final_amount']}")
