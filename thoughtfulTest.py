# Author: Ricardo Munoz Romero
# Date: 2025-03-13
# Description: This algorithm classifies packges into three categories based on their dimesiions and mass 
# Input: width (cm), height (cm), length (cm) and mass (kg)
# Output: REJECTED, SPECIAL, STANDARD

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


print(sort(150, 150, 150, 20))  # Should be REJECTED (both bulky and heavy)
print(sort(150, 150, 150, 10))  # Should be SPECIAL (bulky but not heavy)
print(sort(150, 150, 150, 30))  # Should be REJECTED (both bulky and heavy)
print(sort(80, 150, 100, 40))   # Should be REJECTED (both bulky and heavy)
print(sort(80, 100, 100, 20))   # Should be SPECIAL (exactly at heavy threshold)
print(sort(80, 90, 100, 10))    # Should be STANDARD (neither bulky nor heavy)
print(sort(100, 100, 100, 20))  # Should be REJECTED (exactly at heavy and bulky threshold)
print(sort(100, 100, 100, 10))  # Should be SPECIAL (xactly at bulky threshold)
print(sort(100, 90, 100, 5))    # Should be STANDARD (neither bulky nor heavy)
print(sort('a', 90, 100, 10))   # Should raise TypeError
print(sort(0, 90, 0, 5))        # Should raise ValueError