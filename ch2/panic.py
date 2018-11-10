phrase = "Don't panic!"
plist = list(phrase)

'''Changes the phrase "Don't panic!" to read "on tap"
   using only list methods'''

# initial state
print(phrase)
print(plist)
print()

# remove last 4 characters
for i in range(4):
    plist.pop()

# remove first character and apostrophe
plist.pop(0)
plist.remove("'")

# swap the last two by popping both then extending
plist.extend([plist.pop(), plist.pop()])

# pops and inserts the space
plist.insert(2, plist.pop(3))

# outputs result
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
