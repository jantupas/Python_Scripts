# Dictionary is a collection that is undordered, changeable (mutable) and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# print(person, type(person))

# Constructor
person2 = dict(first_name='Sara', last_name='Williams', age='28')
# print(person2, type(person2))

# Get a value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person3 = person.copy()
person3['city'] = 'Boston'
print(person3)

# Remove item
del (person['age'])
person.pop('phone')

print(person)

# Clear
person.clear()
print(person)

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[0]['name'])
