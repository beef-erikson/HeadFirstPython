phrase = "Don't panic!"
plist = list(phrase)

'''Changes the phrase "Don't panic!" to read "on tap"
   using only square bracket notation'''

# initial state
print(phrase)
print(plist)
print()

# grabs "on"
new_phrase = ''.join(plist[1:3])

# adds "tap" individually
new_phrase += ''.join([plist[5], plist[4], plist[7], plist[6]])

# outputs result
print(plist)
print(new_phrase)
