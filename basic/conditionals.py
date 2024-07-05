# If/Else

x = 25
y = 25
# Comparison operators

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# If/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greated than 2 and less than or equal to 10')

# Logical operators (and, or, not)
# And
if x > 2 and x <= 10:
    print(f'{x} is greated than 2 and less than or equal to 10')

# Or
if x > 2 or x <= 10:
    print(f'{x} is greated than 2 and less than or equal to 10')

# Not
if not (x == y):
    print(f'{x} is not equal to {y}')

# Membership operators (in, not in)
numbers = [1, 2, 3, 4, 5]

# In
if x in numbers:
    print(x in numbers)

# Not in
if x not in numbers:
    print(x not in numbers)

# Identity operators (is, is not) - compare objects if the same object and same memory locaiton
# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)
