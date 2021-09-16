scroll = list(range(1,11))
for nomber in scroll:
    print(nomber + 1)

text = input("Напиши что-нибудь:\n")
for char in text:
    print(char)


#Оценки. Создать список из словарей с оценками учеников разных классов школы
school = [
    {'school_class': '4a', 'scores': [3,4,5,4,3]},
    {'school_class': '4b', 'scores': [3,3,4,5,2]},
    {'school_class': '4c', 'scores': [5,4,2,4,5]},
    {'school_class': '4d', 'scores': [3,4,4,5,2]},
    {'school_class': '4f', 'scores': [3,4,4,3,3]},
    ]
secondary_school = 0
count =0
#Посчитать и вывести средний балл по каждому классу.
#Посчитать и вывести средний балл по всей школе.
for a in school:
    for score in a['scores']:
        secondary_school += score
        count +=1
        
    mean = sum(a['scores'])/ len(a['scores'])
    print(f"Средня оценка по классу {a['school_class']} : {mean}")
print(f"Средняя оценка по школе {secondary_school / count}")
