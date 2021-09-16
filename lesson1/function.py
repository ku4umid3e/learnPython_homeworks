# Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два
#  параметра, приводит их к строке и отдает объединенными через разделитель
#  delimiter
def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'
# Вызовите функцию, передав в нее два аргумента "Learn" и "python", положите
#  результат в переменную и выведите ее значение на экран 
learn_python = get_summ('Learn', 'python')
print(learn_python)
#Сделайте так, чтобы результирующая строка выводилась заглавными буквами
print(learn_python.upper())