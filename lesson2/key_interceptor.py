def hellow_user():
    try:
        while True:
            question = input("Как дела?\n")
            if question == "Хорошо":
                break
            else:
                continue
    except(KeyboardInterrupt):
        print('\nПока!')

hellow_user()

#Задание 2

def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            print(price)
        else:
            print(price - (price * discount / 100))
    except(ValueError, TypeError):
        print('ОШИБКА!')

discounted("10000", "15", 20.5)