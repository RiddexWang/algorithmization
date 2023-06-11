my_list = [1, 2, 3, 4, 5, 1, 6, 7, 8]

repeated_elements = set()

for element in my_list:
    if my_list.count(element) > 1:
        repeated_elements.add(element)

if len(repeated_elements) > 0:
    print(f"В списке есть повторяющиеся элементы: {repeated_elements}")
else:
    print("В списке нет повторяющихся элементов")