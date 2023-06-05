if __name__ == '__main__':
    while True:
        word = input("Введите слово: ")
        if word.lower() == "стоп":
            break
        elif "ф" in word.lower():
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")