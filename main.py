if __name__ == '__main__':
#Первый вариант
    print('Первый вариант')
    pass_1 = input()
    pass_2 = input()

    if pass_2 == pass_1:
        print('Пароль принят')
    else: print('Пароль не принят')

#Второй вариант
    print('Второй вариант')
    if input() == input():
        print('Пароль принят')
    else:
        print('Пароль не принят')

#Третий вариант
    print('Третий вариант')
    print('Пароль принят' if input() == input() else 'Пароль не принят')

