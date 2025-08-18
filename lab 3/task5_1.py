from typing import Callable


_ABSOLUTE_ZERO_BY_UNIT = {
	"celsius": -273.15,
	"fahrenheit": -459.67,
	"kelvin": 0.0,
	"rankine": 0.0,
}


_UNIT_ALIASES = {
	"c": "celsius",
	"cel": "celsius",
	"celsius": "celsius",
	"°c": "celsius",
	"degc": "celsius",
	"f": "fahrenheit",
	"fahrenheit": "fahrenheit",
	"°f": "fahrenheit",
	"degf": "fahrenheit",
	"k": "kelvin",
	"kelvin": "kelvin",
	"r": "rankine",
	"rankine": "rankine",
	"°r": "rankine",
	"degr": "rankine",
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
			f"Unsupported unit '{unit}'. Use one of: celsius, fahrenheit, kelvin, rankine"
		) from exc


def _validate_not_below_absolute_zero(value: float, unit: str) -> None:
	"""Raise ValueError if the given temperature is below absolute zero for the unit."""
	absolute_zero = _ABSOLUTE_ZERO_BY_UNIT[unit]
	# Allow tiny negative epsilon to account for floating-point artifacts
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
	raise AssertionError("Unhandled unit in _from_kelvin")


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
	"""Convert temperature between Celsius, Fahrenheit, Kelvin, and Rankine.

	Args:
		value: Numeric temperature value to convert.
		from_unit: Unit of the input value (case-insensitive). Accepts aliases like
			"C", "Celsius", "F", "Fahrenheit", "K", "Kelvin", "R", "Rankine".
		to_unit: Target unit. Same accepted set as from_unit.

	Returns:
		Converted temperature as a float.

	Raises:
		TypeError: If units are not strings.
		ValueError: If units are unsupported or the value is below absolute zero.

	Strategy:
		Normalize units, validate against absolute zero using the source unit,
		convert to Kelvin as a stable intermediary, then convert to the target unit.
	"""
	canonical_from = _normalize_unit(from_unit)
	canonical_to = _normalize_unit(to_unit)
	if canonical_from == canonical_to:
		_validate_not_below_absolute_zero(value, canonical_from)
		return float(value)

	_validate_not_below_absolute_zero(value, canonical_from)
	value_kelvin = _to_kelvin(float(value), canonical_from)
	return _from_kelvin(value_kelvin, canonical_to)


if __name__ == "__main__":
	print("Examples:")
	print("0 C -> K:", convert_temperature(0, "C", "K"))
	print("100 C -> F:", convert_temperature(100, "C", "F"))
	print("32 F -> C:", convert_temperature(32, "F", "C"))
	print("300 K -> F:", convert_temperature(300, "K", "F"))
	print("491.67 R -> C:", convert_temperature(491.67, "R", "C"))


