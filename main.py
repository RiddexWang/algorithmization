if __name__ == '__main__':
    import random

    correct_answers = 0
    incorrect_answers = 0

    while incorrect_answers < 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = input(f"{a} + {b} = ")
        if int(answer) == a + b:
            correct_answers += 1
            print("Правильно!")
        else:
            incorrect_answers += 1
            print("Ответ неверный")

    print(f"Игра окончена. Правильных ответов: {correct_answers}")