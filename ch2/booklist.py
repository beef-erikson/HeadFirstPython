book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(booklist)

print(''.join(booklist[0:3]))
print(''.join(booklist[-6:]))

backwards = booklist[::-1]
print(''.join(backwards))

every_other = booklist[::2]
print(''.join(every_other))

slice = ''.join(booklist[4:14])
print(slice)

slice_backwards = ''.join(booklist[13:3:-1])
print(slice_backwards)

for char in booklist[4:16]:
    print('\t', char)
for char in booklist[17:23]:
    print('\t'*2, char)
for char in booklist[-6:]:
    print('\t'*3, char)
