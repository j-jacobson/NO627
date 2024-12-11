from itertools import permutations
from sympy.ntheory import isprime

# The numbers to use, ensuring we have one repeat (e.g., repeating 1)
numbers = [2, 7, 5, 6, 9, 3, 10, 6, 4, 1, 8]

# Fixed positions: 2, 3, 1, and 6 are locked in their positions
fixed_positions = {0: 2, 5: 3, 9: 1, 3: 6, 7: 6}

# Extract the numbers that can be permuted
to_permute = [num for i, num in enumerate(numbers) if i not in fixed_positions]

# Generate permutations and check for prime
valid_primes = []
num_sols = 0
for perm in permutations(to_permute):
    # Reconstruct the full sequence with fixed numbers in their positions
    full_sequence = []
    perm_index = 0
    for i in range(len(numbers)):
        if i in fixed_positions:
            full_sequence.append(fixed_positions[i])
        else:
            full_sequence.append(perm[perm_index])
            perm_index += 1

    num = int(''.join(map(str, full_sequence)))
    if isprime(num):
        valid_primes.append(num)
        print(num)
        num_sols += 1

print(f"Number of solutions: {num_sols}")

