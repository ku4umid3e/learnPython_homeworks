def sort_by_age(age):
    """функцию, которая по возрасту определит, чем должен заниматься
    пользователь: учиться в детском саду, школе, ВУЗе или работать"""
    if age <= 6:
        return 'Малышь, тебе надо в детский сад!'
    elif age <= 17:
        return 'Тебе в школу!'
    elif age <= 23:
        return 'Тебе в ВУЗ'
    else:
        return 'Работать.'

print(sort_by_age(age= int(input('Сколько вам лет?\n'))))


def string_comparison(string1, string2):
    """Функция, которая принимает на вход две строки и сравнивает их."""
    if not isinstance(string1, str) or not isinstance(string2, str):
        return 0
    if string1 == string2:
        return 1      
    if string1 != string2 and string2 =='learn':
        return 3
    if len(string1) > len(string2):
        return 2
    

print(string_comparison('hellow', 'learn'))
print(string_comparison('hi', 'learn'))
print(string_comparison(1, 'hellow'))
print(string_comparison('hellow', 'hellow'))
print(string_comparison('hellow world', 'hellow'))
print(string_comparison(1, 1))
print(string_comparison('hellow', 1))

