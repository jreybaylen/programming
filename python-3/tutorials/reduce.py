import functools

words = [ 'H', 'E', 'L', 'L', 'O' ]
word = functools.reduce(lambda x, y: (x + y).lower(), words)

print(word)