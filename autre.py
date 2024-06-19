import random

def generate_number(n):
    if n <= 0:
        return ""

    # Initialize the result list with the first digit
    result = [random.choice(['0', '1', '2', '3'])]
    
    while len(result) < n:
        # Generate a random digit different from the last one
        next_digit = random.choice(['0', '1', '2', '3'])
        while next_digit == result[-1]:
            next_digit = random.choice(['0', '1', '2', '3'])
        result.append(next_digit)

    return ''.join(result)

# Example usage:
n = 10
generated_number = generate_number(n)
print(f"Generated number of length {n}: {generated_number}")