students_list = [
    ('John Doe', 'A', 30),
    ('Foo Bar', 'B', 31),
    ('Jane Doe', 'C', 32),
    ('Fuzzy Doe', 'D', 33),
    ('Wuzzy Doe', 'F', 34)
]
students_tuple = (
    ('John Doe', 'A', 30),
    ('Foo Bar', 'B', 31),
    ('Jane Doe', 'C', 32),
    ('Fuzzy Doe', 'D', 33),
    ('Wuzzy Doe', 'F', 34)
)

name = lambda names: names[0]
score = lambda scores: scores[1]
age = lambda ages: ages[2]

students_list.sort(key=name)
students = sorted(students_tuple, key=score)

for student in students_list:
    print(student)
print('------------------')
for student in students:
    print(student)