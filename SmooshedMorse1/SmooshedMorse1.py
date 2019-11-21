# From u/Cosmologicon at https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

import string

morse_dictionary = {
    'a' : ".-",
    'b' : "-...",
    'c' : "-.-.",
    'd' : "-..",
    'e' : ".",
    'f' : "..-.",
    'g' : "--.",
    'h' : "....",
    'i' : "..",
    'j' : ".---",
    'k' : "-.-",
    'l' : ".-..",
    'm' : "--",
    'n' : "-.",
    'o' : "---",
    'p' : ".--.",
    'q' : "--.-",
    'r' : ".-.",
    's' : "...",
    't' : "-",
    'u' : "..-",
    'v' : "...-",
    'w' : ".--",
    'x' : "-..-",
    'y' : "-.--",
    'z' : "--..",
    '1' : ".----",
    '2' : "..---",
    '3' : "...--",
    '4' : "....-",
    '5' : ".....",
    '6' : "-....",
    '7' : "--...",
    '8' : "---..",
    '9' : "----.",
    '0' : "-----"
}

# Map input
lines = open('enable1.txt','r').readlines()
print(str(len(lines)) + " lines parsed")

# Parse lines
morse = []
for line in lines:
    morseline = ''.join(morse_dictionary[char] for char in line if char in morse_dictionary)
    morse.append(morseline)
print(str(len(morse)) + " lines converted")

# Challenges and verification
dots = 0
dashes = 0
for line in morse:
    for char in line:
        if char == '.': dots += 1
        else: dashes += 1

print(str(dots) + " dots counted")
print(str(dashes) + " dashes counted")

# Challenge 1
unique = {}
for line in morse:
    if line not in unique.keys():
        unique[line] = 1
    else:
        unique[line] += 1
for item in unique.items():
    if item[1] == 13:
        challenge1 = item[0]
        break

# Challenge 2
all_max_dashes = []
for sequence in morse:
    consecutive_dashes = 0
    max_dashes = 0
    for char in sequence:
        if char == '-':
            consecutive_dashes += 1
            if consecutive_dashes > max_dashes:
                max_dashes = consecutive_dashes
        else:
            consecutive_dashes = 0
    all_max_dashes.append(max_dashes)

for index, max_dashes in enumerate(all_max_dashes):
    if max_dashes == 15:
        challenge2 = lines[index].split().pop() # pop() to remove line break character at the end
        challenge2 = str(challenge2)
        break

# Challenge 3
challenge3 = ''
for index, word in enumerate(lines):
    if len(word) == 21:
        word_dots = 0
        word_dashes = 0
        for char in morse[index]:
            if char == '.': word_dots += 1
            else: word_dashes += 1
            if word_dots == word_dashes:
                challenge3 = word.split().pop() # pop() to remove line break character at the end
                challenge3 = str(challenge3)
    else: continue
    if challenge3:
        break

# Challenge 4
for word in lines:
    if len(word) == 13:
        sequence = ''.join(morse_dictionary[char] for char in line if char in morse_dictionary)
        palindrome = True
        i = 0
        while (i <= len(sequence) // 2 - 1):
            if sequence[i] != sequence[len(sequence) - i - 1]:
                palindrome = False
                break
            i += 1
        if palindrome:
            challenge4 = word.split().pop() # pop() to remove line break character at the end
            challenge4 = str(challenge4)

# Challenge 5
possible_sequences = [".", "-"]
for sequence in possible_sequences:
    sequence.append(".")
    possible_sequences.append(sequence.append("-"))
#for sequence in morse:


# Print answers
print("\"" + challenge1 + "\" is code for 13 words")
print("\"" + challenge2 + "\" in Morse has 15 consecutive dashes")
print("\"" + challenge3 + "\" is another perfectly-balanced word")
print("\"" + challenge4 + "\" is the only 13-letter palindrome in Morse")
print("\n" + len(possible_sequences) + " possible sequences were generated")
#print(challenge5 + " do not appear in the list of translated words")