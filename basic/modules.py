# Module is a file containing a set of functions to include in application
# core python modules, modules you can install using pip, custom modules

# Core modules
import datetime
from datetime import date
# import time
from time import time

# Pip module
from camelcase import CamelCase

# Custom module
from validator import validate_email

today1 = datetime.date.today()
today2 = date.today()
# timestamp = time.time()
timestamp2 = time()

print(today2)
print(timestamp2)

# Pip module
c = CamelCase()
print(c.hump('hello there world'))

# Custom module
email = 'test@test.com'

if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')
