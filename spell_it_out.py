# spell_it_out.py

# Ask the user for a word
word = input("Enter a word: ")

print("\n--- Letters on separate lines ---")
# Use a for loop to print each letter of the word on its own line
for letter in word:
    print(letter)

print("\n--- Numbered letters ---")
# Use a second loop with a counter/enumerate to print the letters numbered
for i, letter in enumerate(word, 1):
    # Print formatted with comma spacing up to the last item
    end_char = ", " if i < len(word) else "\n"
    print(f"{i}. {letter}", end=end_char)

# Finish by printing how many letters the word has
print(f"The word '{word}' has {len(word)} letters.")