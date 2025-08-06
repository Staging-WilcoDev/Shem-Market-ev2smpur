def all_even(numbers):
    """
    Returns True if all numbers in the list are even, False otherwise.
    
    Args:
        numbers (list): A list of numbers to check
        
    Returns:
        bool: True if all numbers are even, False otherwise
    """
    return all(num % 2 == 0 for num in numbers)


def any_negative(numbers):
    """
    Returns True if any number in the list is negative, False otherwise.
    
    Args:
        numbers (list): A list of numbers to check
        
    Returns:
        bool: True if any number is negative, False otherwise
    """
    return any(num < 0 for num in numbers)


# Example usage and testing
if __name__ == "__main__":
    # Test all_even function
    print("Testing all_even function:")
    print(f"all_even([2, 4, 6, 8]): {all_even([2, 4, 6, 8])}")  # Should be True
    print(f"all_even([2, 4, 5, 8]): {all_even([2, 4, 5, 8])}")  # Should be False
    print(f"all_even([]): {all_even([])}")  # Should be True (empty list)
    
    # Test any_negative function
    print("\nTesting any_negative function:")
    print(f"any_negative([1, 2, 3]): {any_negative([1, 2, 3])}")  # Should be False
    print(f"any_negative([1, -2, 3]): {any_negative([1, -2, 3])}")  # Should be True
    print(f"any_negative([-1, -2, -3]): {any_negative([-1, -2, -3])}")  # Should be True
    print(f"any_negative([]): {any_negative([])}")  # Should be False (empty list)
