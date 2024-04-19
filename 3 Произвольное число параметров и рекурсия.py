def test(txt, *params, **second):
    print(txt, params, second)
    for key, value in second.items():
        print(key, value)


test('Что-то здесь', 12, 13, 14, name='Anton', second_name='Kapustin')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
#Ответ верный получается, но сам не смог додуматься как написать функцию для факториала





