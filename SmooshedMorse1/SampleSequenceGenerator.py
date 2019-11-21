# Parameters
max_length = 13
possible_values = [".", "-"]

# Initialize array
possible_sequences = []
for n in range(len(possible_values) ** max_length):
    possible_sequences.append([possible_values[0] * max_length])

print(str(len(possible_sequences)) + " possible sequences calculated")
print("Populating sequences...")

i = 0
for sequence in possible_sequences:
    for character in sequence:
