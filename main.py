if __name__ == '__main__':
    color1 = input("Введите первый цвет: ")
    color2 = input("Введите второй цвет: ")

    if (color1 == "Красный" and color2 == "Синий") or (color1 == "Синий" and color2 == "Красный"):
        print("Фиолетовый")
    elif (color1 == "Красный" and color2 == "Желтый") or (color1 == "Желтый" and color2 == "Красный"):
        print("Оранжевый")
    elif (color1 == "Синий" and color2 == "Желтый") or (color1 == "Желтый" and color2 == "Синий"):
        print("Зеленый")
    else:
        print("Ошибка! Введите название одного из основных цветов: ККрасный, Синий или Желтый.")