def my_func(**kwargs):
    return ' '.join(kwargs.values())


print(my_func(name='Andrei', surname="Galich", year='1988', city="SPb", phone='1234567'))
