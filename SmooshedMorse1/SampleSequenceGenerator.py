# Creates a list containing all possible sequences, as strings,
# of length max_length given a list of possible character values

# Parameters
max_length = 13
possible_values = [".", "-"]

def generate_sequences(length, values):
    current_sequences = values
    for dimension in range(1, length):
        current_sequences = add_dimension(current_sequences, values)
    return current_sequences

def add_dimension(current_sequences, values_to_add):
    new_sequences = []
    for sequence in current_sequences:
        for value in values_to_add:
            new_sequences.append(sequence + value)
    return new_sequences

def verify_uniqueness(sequence_list):
    unique_sequences = []
    for sequence in sequence_list:
        if sequence in unique_sequences:        # Could also use .count(), which takes up less memory but is slower
            return False
        else:
            unique_sequences.append(sequence)
    return True

possible_sequences = generate_sequences(max_length, possible_values)

txtout = open('sequences.txt', 'w+')
for sequence in possible_sequences:
    txtout.write(sequence + "\n")
print(str(len(possible_sequences)) + " possible sequences generated")
print("All sequences are unique: " + str(verify_uniqueness(possible_sequences)))