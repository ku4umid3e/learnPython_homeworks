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
            return price
        else:
            return price - (price * discount / 100)
    except(ValueError, TypeError):
        return 'ОШИБКА!'

print(discounted("10000", "15", 20.5))
print(discounted(100, 2))
print(discounted(100, "3"))
print(discounted("100", "4.5"))
print(discounted("five", 5))
print(discounted("сто", "десять"))
print(discounted(100.0, 5, "10"))