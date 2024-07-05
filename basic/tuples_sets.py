# Tuple is a collection which is ordered and unchangeable - immutable

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# Constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
# If tuple only has 1 element, must add trailing comma
fruits3 = ('Apples',)

# print(fruits, fruits2, fruits3)

# Get value
print(fruits[1])

# Can't change value, below will not work
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))

# Set is a collection which is unordered and unindexed. No duplicate members
fruits_set = {'Apples', 'Oranges', 'Mango'}
fruits_set2 = set(('Apples', 'Oranges', 'Mango'))

# print(fruits_set, fruits_set2)
# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

# Add duplicate - won't work
fruits_set.add('Apples')

# Clear set - empty set
fruits_set.clear()
print(fruits_set)

# Delete set
del fruits_set
