def test(txt, *params, **second):
    print(txt, params, second)
    for key, value in second.items():
        print(key, value)


test('Что-то здесь', 12, 13, 14, name='Anton', second_name='Kapustin')


def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)


print(summa(6))





