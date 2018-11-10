vowels = ('a', 'e', 'i', 'o', 'u')
found = {}

'''Vowel Histogram for getting number of vowels from provided
   user input.'''


# gets input from user to process
word = input("\nProvide a word or phrase to search for vowels: ")
print()

# searches word and adds value to any vowels matching list
for letter in word:
    if letter in vowels:
        # initializes new dict entry if not present and increases
        found.setdefault(letter, 0)
        found[letter] += 1

# sort dict and find number of vowel occurrences
for key, value in sorted(found.items()):
    print(key, 'was found', value, 'time(s).')
