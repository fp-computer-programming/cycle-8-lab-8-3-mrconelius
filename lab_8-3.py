# Function to find the sum of values from 1 to n using a while loop.
def sum_to(n):
    """
    This function takes an integer n and returns the sum of all values from 1 to n.

    Parameters:
    - n (int): The input integer.

    Returns:
    - int: The sum of values from 1 to n.
    """
    # Initialize variables
    total = 0
    i = 1

    # Use a while loop to iterate until i is greater than n
    while i <= n:
        total += i
        i += 1

    return total

# Test the function with an example value
result = sum_to(5)
print(f"The sum of values from 1 to 5 is: {result}")
