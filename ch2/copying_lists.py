first = [1, 2, 3, 4, 5]

# Bad. Changes both
second = first
second.append(6)

print(second)
print(first)

# Good!
third = second.copy()
third.append(7)

print(third)
print(second)
