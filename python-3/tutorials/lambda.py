double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda fname, lname: '{} {}'.format(fname, lname)

print(double(5))
print(multiply(5, 2))
print(add(5, 2, 3))
print(full_name('John', 'Doe'))