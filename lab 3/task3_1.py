from typing import Dict, List, Optional, Tuple


def calculate_energy_charge(units_consumed: int, slabs: Optional[List[Tuple[Optional[int], float]]] = None) -> float:
	"""Calculate the base energy charge for the given units using tiered slabs."""
	if units_consumed < 0:
		raise ValueError("Units consumed cannot be negative")

	default_slabs: List[Tuple[Optional[int], float]] = [
		(100, 1.5),   # first 100 units @ 1.5
		(100, 2.5),   # next 100 units @ 2.5
		(200, 4.0),   # next 200 units @ 4.0
		(None, 6.0),  # remaining units @ 6.0
	]

	rate_slabs = slabs if slabs is not None else default_slabs
	remaining_units = units_consumed
	amount = 0.0

	for slab_limit, slab_rate in rate_slabs:
		if remaining_units <= 0:
			break
		units_in_this_slab = remaining_units if slab_limit is None else min(remaining_units, slab_limit)
		amount += units_in_this_slab * slab_rate
		remaining_units -= units_in_this_slab

	return amount


def calculate_power_bill_with_taxes(
	units_consumed: int,
	slabs: Optional[List[Tuple[Optional[int], float]]] = None,
	tax_config: Optional[Dict[str, float]] = None,
) -> Dict[str, float]:
	"""Return a detailed bill including taxes.

	Args:
		units_consumed: Non-negative integer units consumed
		slabs: Optional custom slabs [(limit, rate), ...] with last limit optionally None
		tax_config: Optional dict with keys:
			- 'fuel_surcharge_percent' (default 5.0)
			- 'fixed_charge' (default 50.0)
			- 'gst_percent' (default 18.0)
	"""

	if units_consumed < 0:
		raise ValueError("Units consumed cannot be negative")

	defaults: Dict[str, float] = {
		"fuel_surcharge_percent": 5.0,
		"fixed_charge": 50.0,
		"gst_percent": 18.0,
	}
	config = {**defaults, **(tax_config or {})}

	energy_charge = calculate_energy_charge(units_consumed, slabs)
	fuel_surcharge = energy_charge * (config["fuel_surcharge_percent"] / 100.0)
	subtotal_before_gst = energy_charge + fuel_surcharge + config["fixed_charge"]
	gst_amount = subtotal_before_gst * (config["gst_percent"] / 100.0)
	total_amount = subtotal_before_gst + gst_amount

	return {
		"energy_charge": round(energy_charge, 2),
		"fuel_surcharge": round(fuel_surcharge, 2),
		"fixed_charge": round(config["fixed_charge"], 2),
		"gst_amount": round(gst_amount, 2),
		"total_amount": round(total_amount, 2),
	}


def print_bill(units_consumed: int) -> None:
	breakdown = calculate_power_bill_with_taxes(units_consumed)
	print(f"Units consumed: {units_consumed}")
	print(f"Energy charge: {breakdown['energy_charge']:.2f}")
	print(f"Fuel surcharge: {breakdown['fuel_surcharge']:.2f}")
	print(f"Fixed charge: {breakdown['fixed_charge']:.2f}")
	print(f"GST: {breakdown['gst_amount']:.2f}")
	print("-" * 28)
	print(f"Total bill: {breakdown['total_amount']:.2f}")


if __name__ == "__main__":
	user_input = input("Enter units consumed (non-negative integer): ").strip()
	try:
		units = int(user_input)
		if units < 0:
			raise ValueError
	except ValueError:
		print("Invalid input. Please enter a non-negative integer.")
	else:
		print_bill(units)

