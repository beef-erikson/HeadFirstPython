vowels = set('aeiou')

'''Set example to see what vowels are being used with user input'''


# gets input from user to process
word = input("\nProvide a word or phrase to search for vowels: ")

# uses intersection with word and prints result
found = vowels.intersection(word)
for vowel in found:
    print(vowel)
