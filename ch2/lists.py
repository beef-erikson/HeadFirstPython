prices = []
temps = [32.0, 212.0, 0.0, 81.6, 100.0, 45.3]
words = ['hello', 'world']
car_details = ['Toyota', 'RAV4', 2.2, 60807]
odds_and_ends = [[1, 2, 3], ['a', 'b', 'c'], ['One', 'Two', 'Three']]
everything = [prices, temps, words, car_details, odds_and_ends]

print(everything[4][2][2])

found = []
print(len(found))

found.append('a')
found.append('e')
found.append('i')
found.append('o')

print(len(found))
print(found)

if 'u' not in found:
    found.append('u')

print(found)

nums = [1, 2, 3, 4]
print(nums)

# removes value
nums.remove(3)
print(nums)

# removes last
nums.pop()
print(nums)

# removes first indexed value
nums.pop(0)
print(nums)

# extends
nums.extend([3, 4])
print(nums)

# inserts at index position
nums.insert(0, 1)
print(nums)

# no value type necessary
nums.insert(2, 'two and a half')
print(nums)
