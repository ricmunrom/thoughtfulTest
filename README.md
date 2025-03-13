# Package Classification System

A simple and efficient algorithm for classifying packages based on their dimensions and mass.

## Description

This program categorizes packages into three distinct classes based on predefined criteria:

- **REJECTED**: Packages that are both bulky and heavy
- **SPECIAL**: Packages that are either bulky or heavy (but not both)
- **STANDARD**: Packages that are neither bulky nor heavy

## Classification Criteria

- **Bulky**: A package is considered bulky if:
  - Its volume is ≥ 1,000,000 cm³, OR
  - Any single dimension (width, height, or length) is ≥ 150 cm

- **Heavy**: A package is considered heavy if:
  - Its mass is ≥ 20 kg

## Usage

```python
# Define the sort function in your script
def sort(width, height, length, mass):
    # Input validation
    if not all(isinstance(param, (int, float)) for param in [width, height, length, mass]):
        raise TypeError("All parameters must be numeric")
    if any(param <= 0 for param in [width, height, length, mass]):
        raise ValueError("All dimensions and mass must be positive values")
    volume = width*height*length
    is_bulky = volume >= 1000000 or width>=150 or height>=150 or length>=150
    is_heavy = mass >= 20
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example usage
result = sort(width=100, height=50, length=30, mass=15)
print(result)  # Output: "STANDARD"
```

## Parameters

- `width` (float): Width of the package in centimeters
- `height` (float): Height of the package in centimeters
- `length` (float): Length of the package in centimeters
- `mass` (float): Mass of the package in kilograms

## Return Value

The function returns one of three string values:
- `"REJECTED"`: Package is both bulky and heavy
- `"SPECIAL"`: Package is either bulky or heavy (but not both)
- `"STANDARD"`: Package is neither bulky nor heavy

## Examples

```python
# Bulky and heavy (REJECTED)
sort(150, 150, 150, 30)  # Output: "REJECTED"

# Bulky but not heavy (SPECIAL)
sort(150, 150, 150, 10)  # Output: "SPECIAL"

# Heavy but not bulky (SPECIAL)
sort(100, 50, 100, 20)  # Output: "SPECIAL"

# Neither bulky nor heavy (STANDARD)
sort(20, 30, 100, 10)  # Output: "STANDARD"
```

## Author

Ricardo Munoz Romero

## Date

2025-03-13
