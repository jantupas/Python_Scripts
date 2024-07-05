# Loop is used to iterate over a sequence

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
    print(f'Current Person: {person}')

# Break - stops on sara
for person in people:
    if person == 'Sara':
        break
    print(f'Current Person: {person}')

# Continue - skips sara but continue after
for person in people:
    if person == 'Sara':
        continue
    print(f'Current Person: {person}')

# Range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')

# While loops exeute a set of statements as long as condition is true
count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1
