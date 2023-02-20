store = (
    ('shirt', 20.00),
    ('pants', 22.00),
    ('sando', 10.00),
    ('polo', 30.00),
    ('jacket', 50.00)
)

to_pesos = lambda data: (data[0], 'PHP {:.2f}'.format(data[1] * 55.10))

store_pesos = map(to_pesos, store)

for product in store_pesos:
    print(product)