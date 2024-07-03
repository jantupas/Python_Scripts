from student import Student

stud1 = Student("Jan", 22, "Makati City")

name = stud1.getName()
age = stud1.getAge()
address = stud1.getAddress()
print(name)
print(age)
print(address)

greet = stud1.greeting()
print(greet)

stud1.setName("Jed")
stud1.setAge(23)
stud1.setAddress("Makati")

name = stud1.getName()
age = stud1.getAge()
address = stud1.getAddress()

print(name)
print(age)
print(address)

greet = stud1.greeting()
print(greet)
