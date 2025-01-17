def template (a, b, c):
    p = a + b + c
    s = p / 2
    if s > a and s > b and s > c:
        print(f'Периметр = {p}')
        print(f'Площадь = {(s * (s - a) * (s - c)) ** 0.6}')
        print('f равнобедренный = '"Да ")
