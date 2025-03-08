from itertools import permutations

the_solution = "AMONG"

# Define available letters
#available_letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
available_letters = {'A', 'B', 'F', 'O', 'G', 'J', 'M', 'N', 'V', 'W', 'X'}

# Wordle constraints
word_length = 5

# Green letters (correct positions, 0-based index)
correct_positions = {2: 'O'}

# Yellow letters (must be included but NOT in these positions)
misplaced_letters = {'G': [0]}

# Gray letters (excluded completely)
excluded_letters = {}

# Forbidden letter pairs (unlikely letter combinations)
forbidden_pairs = {
    "WX", "BX", "KJ", "ZQ", "VZ", "XZ", "JQ", "QK", "QX", "QV", "ZJ", "ZF",
    "VX", "CJ", "JX", "XJ", "JZ", "FQ", "GZ", "QJ", "QP", "YQ", "KZ", "PZ",
    "VJ", "MX", "XZ", "DX", "VX", "HZ", "ZX", "QY", "QG", "JY", "QV", "QW"
}

# Required letter sequences (e.g., if "Q" appears, it must be followed by "U")
required_sequences = {"Q": "QU"}

# Generate all possible permutations of the available letters
valid_permutations = []
for perm in permutations(available_letters, word_length):
    word = ''.join(perm)

    # Check green letter constraints
    if any(word[pos] != letter for pos, letter in correct_positions.items()):
        continue

    # Check yellow letter constraints (must be in the word but in a different position)
    if any(letter not in word or any(word[pos] == letter for pos in positions) for letter, positions in misplaced_letters.items()):
        continue

    # Check gray letters (excluded completely)
    if any(letter in word for letter in excluded_letters):
        continue

    # Check forbidden letter pairs
    if any(pair in word for pair in forbidden_pairs):
        continue

    # Check required sequences (e.g., "Q" must be followed by "U")
    if any(letter in word and required not in word for letter, required in required_sequences.items()):
        continue

    valid_permutations.append(word)

# Function to print the list in columns
def print_columns(word_list, num_columns=15):
    # Print the words in the specified number of columns
    for i in range(0, len(word_list), num_columns):
        print('\t'.join(word_list[i:i + num_columns]))

# Output results
print(f"Found {len(valid_permutations)} valid permutations:")

print_columns(valid_permutations)
#for word in valid_permutations:
#  if(word == the_solution):
#    print(f"{word} <- The Wordle (Do not use for 'Don't Wordle'!)")
#  else:
#    print(word)

print(f"Found {len(valid_permutations)} valid permutations.")

