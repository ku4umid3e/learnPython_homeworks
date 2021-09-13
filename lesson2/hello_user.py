def hellow_user():
    while True:
        question = input("Как дела?\n")
        if question == "Хорошо":
            break

#hellow_user()

question_answer = {
    "Как дела": "Хорошо!",
    "Что делаешь?": "Программирую",
    }

def ask_user(question_answer):
    while True:
        ask = input("Спроси меня 'Как дела' или 'Что делаешь?' скажи 'бай': \n")
        if ask == 'бай':
            break
        else:
            if question_answer.get(ask) is None:
                continue
            else:
                print(question_answer.get(ask))

ask_user(question_answer)
