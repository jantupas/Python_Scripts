# Enumerate
fruits = ["apple", "orange", "lemon"]

for i, fruits in enumerate(fruits):
    print(i, fruits)

# Filter
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)
