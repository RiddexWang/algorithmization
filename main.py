if __name__ == '__main__':
    a = int(input("введите номер места "))
    if a < 1 or a > 54:
        print('Такого места нет')
    elif a % 2 == 0 and a <= 36:
        print('Вверхнее место в купе')
    elif a % 2 != 0 and a <= 35:
        print('Нижннее место в купе')
    elif a % 2 == 0 and a > 36:
        print('Вверхнее боковое место')
    else:
        print('Нижнее боковое место')
