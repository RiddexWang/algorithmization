if __name__ == '__main__':
    def is_leap_year(year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False


    year = int(input("Введите год: "))
    if is_leap_year(year):
        print("Год", year, " - високосный")
    else:
        print("Это год не високосный")