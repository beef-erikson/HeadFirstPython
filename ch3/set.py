vowels = set('aeiou')
word = 'hello'

'''Examples of using set functions
'''

# header
print()
print('---')
print('Examples of using set functions')
print('Vowels set:', sorted(vowels))
print('Word to check against:', word)
print('---')
print()

# example of union between word and vowels
union = vowels.union(set(word))
print('Union of word and vowels')
print(union, '- Unsorted')
print(sorted(list(union)), '- Sorted')
print()

# example of difference between word and vowels
difference = vowels.difference(set(word))
print('Difference of word and vowels')
print(difference)
print()

# example of intersection between word and vowels
intersection = vowels.intersection(set(word))
print('Intersection of word and vowels')
print(intersection)
