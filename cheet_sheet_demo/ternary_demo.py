# if statement
age = 15
# if age < 18:
#     print('kid')
# else:
#     print('adult')
# equivalent ternary operator
print('kid' if age < 18 else 'adult')

# if age < 18:
#     if age < 13:
#         print('kid')
#     else:
#         print('teen')
# else:
#     print('adult')
# equivalent ternary operator
print('kid' if age < 13 else 'teen' if age < 18 else 'adult')
