friends = [
    ('John Doe', 30),
    ('Foo Bar', 31),
    ('Jane Doe', 32),
    ('Fuzzy Doe', 33),
    ('Wuzzy Doe', 34)
]

age = lambda data: data[1] > 33

elders = filter(age, friends)

for elder in elders:
    print(elder)