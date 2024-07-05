# Function is a block of code which runs when called - python use indentation with tabs or spaces

# Create function
def say_hello(name):
    print(f'Hello {name}')


# Default argument
def say_hello_sam(name='Sam'):
    print(f'Hello {name}')


say_hello('John Doe')
say_hello_sam()


# Return values
def get_sum(num1, num2):
    total = num1 + num2
    return total


num = get_sum(5, 10)
print(num)

# Lambda function is a small anonymous function
# Can take any number of arguments, but only have one expression
# Similar to JS arrow functions
get_sum = lambda num1, num2: num1 + num2
num = get_sum(3, 7)
print(num)
