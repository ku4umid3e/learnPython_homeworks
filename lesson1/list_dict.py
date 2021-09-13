#Создайте список из чисел 3, 5, 7, 9 и 10.5
scroll = [3, 5, 7, 9, 10.5]
#Выведите содержимое списка на экран
print(scroll)
#Добавьте в конец списка строку "Python"
scroll.append("Python")
#Выведите длину списка на экран
print(len(scroll))
#Выведите на экран начальный элемент списка
print(scroll[0])
#Выведите на экран последний элемент списка
print(scroll[-1])
#Напечатайте элементы списка со второго
#  по четвертый включительно
print(scroll[1:4])
#Удалите из списка строку "Python"
del(scroll[-1])


#Создайте словарь:{"city": "Москва", "temperature": "20"}
weather = {"city": "Москва", "temperature": "20"}
#Выведите на экран значение ключа city
print(weather['city'])
#Уменьшите значение "temperature" на 5
weather["temperature"] = 15
#Выведите на экран весь словарь
print(weather)
#Проверьте, есть ли в словаре ключ country
if 'country' in weather:
    print("Есть")
else:
    print("Нет")
#Выведите значение по-умолчанию "Россия" для ключа country
print(weather.get("country", "Россия"))
#Добавьте в словарь элемент date со значением "27.05.2019"
weather["date"] = "27.05.2019"
#Выведите на экран длину словаря
print(len(weather))
