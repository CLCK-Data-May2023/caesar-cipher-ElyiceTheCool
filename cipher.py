# Get user sentence as input
user_sentence = input("Please enter a sentence: ")
user_char = list(user_sentence)

# Get character index of each letter in sentence
abc = "abcdefghijklmnopqrstuvwxyz"

encrypted_list = []

for letter in user_char:
    char_index = abc.find(letter)
    encrypted_char = abc[char_index + 5]
    encrypted_list.append(encrypted_char)

encrypted_sentence = "".join(encrypted_list)
print(encrypted_sentence)

# Encrypt by moving index to the right 5 spaces
# Use modelo to take care of indexes larger than 25

# Print full encrypted sentence

