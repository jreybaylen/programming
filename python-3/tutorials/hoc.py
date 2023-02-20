def divisor(x):
    def dividend(y):
        return y / x

    return dividend

divide = divisor(2)

print('{:.2f}'.format(divide(10)))