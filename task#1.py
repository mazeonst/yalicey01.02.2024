""" ЗАДАЧА 1
Необходимо написать функцию transform, которая на вход получает последовательность объектов и возвращает преобразованную последовательность в список вложенных объектов.

Сигнатура функции: def transform(iterable: typing.Iterable) -> list: ...

Пример вызова: transform([1, 2])

Пример 1
Ввод: 1 2
Вывод: [1 [2]]

Пример 2
Ввод: 1 2 3
Вывод: [1 [2 [3]]]

"""

import typing

def transform(iterable: typing.Iterable) -> list:
    if not iterable:
        return []

    nested_result = transform(iterable[1:])

    result = [iterable[0]]

    if nested_result:
        result.append(nested_result)

    return result

input_str = input()
numbers = list(map(int, input_str.split()))

result = transform(numbers)

print(result)