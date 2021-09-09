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