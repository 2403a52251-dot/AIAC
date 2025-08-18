from typing import Dict
_ABSOLUTE_ZERO_BY_UNIT: Dict[str, float] = {
	"celsius": -273.15,
	"fahrenheit": -459.67,
	"kelvin": 0.0,
	"rankine": 0.0,
	"reaumur": -218.52,  # 0.8 * (-273.15)
}


_UNIT_ALIASES: Dict[str, str] = {
	# Celsius
	"c": "celsius",
	"cel": "celsius",
	"celsius": "celsius",
	"°c": "celsius",
	"degc": "celsius",
	# Fahrenheit
	"f": "fahrenheit",
	"fahrenheit": "fahrenheit",
	"°f": "fahrenheit",
	"degf": "fahrenheit",
	# Kelvin
	"k": "kelvin",
	"kelvin": "kelvin",
	# Rankine
	"r": "rankine",
	"rankine": "rankine",
	"°r": "rankine",
	"degr": "rankine",
	# Réaumur
	"re": "reaumur",
	"reaumur": "reaumur",
	"réaumur": "reaumur",
	"°re": "reaumur",
}


def _normalize_unit(unit: str) -> str:
	"""Return canonical unit name from user input; raises on unknown."""
	if not isinstance(unit, str):
		raise TypeError("unit must be a string")
	key = unit.strip().lower()
	try:
		return _UNIT_ALIASES[key]
	except KeyError as exc:
		raise ValueError(
			f"Unsupported unit '{unit}'. Use one of: Celsius (C), Fahrenheit (F), Kelvin (K), Rankine (R), Réaumur (Re)."
		) from exc


def _validate_not_below_absolute_zero(value: float, unit: str) -> None:
	"""Raise ValueError if the given temperature is below absolute zero for the unit."""
	absolute_zero = _ABSOLUTE_ZERO_BY_UNIT[unit]
	if value < absolute_zero - 1e-9:
		raise ValueError(
			f"Temperature {value} {unit} is below absolute zero ({absolute_zero} {unit})."
		)


def _to_kelvin(value: float, unit: str) -> float:
	"""Convert a temperature to Kelvin from the canonical unit name."""
	if unit == "kelvin":
		return value
	if unit == "celsius":
		return value + 273.15
	if unit == "fahrenheit":
		return (value + 459.67) * 5.0 / 9.0
	if unit == "rankine":
		return value * 5.0 / 9.0
	if unit == "reaumur":
		return value * 1.25 + 273.15  # (Re -> C) then +273.15
	raise AssertionError("Unhandled unit in _to_kelvin")


def _from_kelvin(value_kelvin: float, unit: str) -> float:
	"""Convert a temperature from Kelvin to the canonical unit name."""
	if unit == "kelvin":
		return value_kelvin
	if unit == "celsius":
		return value_kelvin - 273.15
	if unit == "fahrenheit":
		return value_kelvin * 9.0 / 5.0 - 459.67
	if unit == "rankine":
		return value_kelvin * 9.0 / 5.0
	if unit == "reaumur":
		return (value_kelvin - 273.15) * 0.8
	raise AssertionError("Unhandled unit in _from_kelvin")


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
	"""Convert temperature between Celsius, Fahrenheit, Kelvin, Rankine, and Réaumur.

	Args:
		value: Numeric temperature value to convert.
		from_unit: Unit of the input value (e.g., "C", "F", "K", "R", "Re").
		to_unit: Target unit (same accepted set as from_unit).

	Returns:
		Converted temperature as a float.

	Raises:
		TypeError: If units are not strings.
		ValueError: If units are unsupported or the value is below absolute zero.
	"""
	canonical_from = _normalize_unit(from_unit)
	canonical_to = _normalize_unit(to_unit)
	if canonical_from == canonical_to:
		_validate_not_below_absolute_zero(value, canonical_from)
		return float(value)

	_validate_not_below_absolute_zero(value, canonical_from)
	value_kelvin = _to_kelvin(float(value), canonical_from)
	return _from_kelvin(value_kelvin, canonical_to)


def _print_instructions() -> None:
	print("Temperature Converter")
	print("----------------------")
	print("Supported units:")
	print("- Celsius: C, °C, Celsius")
	print("- Fahrenheit: F, °F, Fahrenheit")
	print("- Kelvin: K, Kelvin")
	print("- Rankine: R, °R, Rankine")
	print("- Réaumur: Re, °Re, Réaumur")
	print()
	print("How to use:")
	print("1) Enter the numeric temperature value (e.g., 100)")
	print("2) Enter the source unit (e.g., C)")
	print("3) Enter the target unit (e.g., F)")
	print("We will print the converted result.")
	print()
	print("Examples:")
	print("- 100 C -> F = 212")
	print("- 80 Re -> C = 100")
	print("- 32 F -> C = 0")
	print()


if __name__ == "__main__":
	_print_instructions()
	while True:
		value_str = input("Enter value (or blank to exit): ").strip()
		if value_str == "":
			print("Goodbye!")
			break
		try:
			value = float(value_str)
		except ValueError:
			print("Please enter a valid number for the value.")
			continue
		from_u = input("From unit (C/F/K/R/Re): ").strip()
		to_u = input("To unit (C/F/K/R/Re): ").strip()
		try:
			result = convert_temperature(value, from_u, to_u)
			print(f"Result: {value} {from_u} = {result:.2f} {to_u}")
		except (ValueError, TypeError) as exc:
			print(f"Error: {exc}")
		print()


