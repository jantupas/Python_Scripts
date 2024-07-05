name = 'Brad'
age = 37

# Concatenate
# print('Hello, my nme is ' + name + ' and I am ' + str(age))

# String Formatting

# Argument by position
# print('My name is {name} and I ame {age}'.format(name = name, age = age))

# F-Strings (3.6+)
# print(f'My name is {name} and I am {age}')

# String Methods
s = 'hello world'

# Capitalize String
print(s.capitalize())

# Uppercase
print(s.upper())

# Lowercase
print(s.lower())

# Swap
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numberic
print(s.isnumeric())
