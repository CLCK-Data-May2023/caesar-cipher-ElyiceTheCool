# Get input and break it into pieces
user_sentence = input("Please enter a sentence: ").lower()
user_char = list(user_sentence)

abc = "abcdefghijklmnopqrstuvwxyz"
encrypted_list = []

# Get character index of each letter in sentence
for letter in user_char:
    char_index = abc.find(letter)
    if letter == " ":
        encrypted_list.append(letter)
    elif letter.isalnum() == False:
        encrypted_list.append(letter)
    else:
        # Shifted to the right 5
        encrypted_char = abc[(char_index + 5) % 26]
        encrypted_list.append(encrypted_char)

# Put the letters back together and present
encrypted_sentence = "".join(encrypted_list)
print(encrypted_sentence)
