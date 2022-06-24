"""Практика 17.9.1 """

while True:   # Цикл для ввода данных пользователя
    try:
        namder = list(map(int,input("Введите число через пробел:").split( )))
    except Exception:
        print("Ошибка не корректный ввод")
    else:
        break



while True:
    try:
        namder_2 = list(map(int, input(f'Введите число от {min(list(namder))} до {max(list(namder))}: ').split()))
        if min(list(namder_2)) < min(list(namder)) or min(list(namder_2)) > max(list(namder)):
            raise ValueError
    except ValueError:
        print(f"Нужно ввести число от {min(list(namder))} до {max(list(namder))}!")
    else:
        break

namder_list, num = list(map(int, namder)), list(map(int,namder_2))
namder_list.extend(num)
print("Список чисел:", namder_list)

# Сортировка
for i in range(len(namder_list)):
    for j in range(len(namder_list) - i - 1):
        if namder_list[j] > namder_list[j + 1]:
            namder_list[j], namder_list[j + 1] = namder_list[j + 1], namder_list[j]

sort = namder_list
print(f"Сортировка чисел",sort)

#Двоичный поиск

def binary_search(sort, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if sort[middle] == element:
        return middle
    elif element < sort[middle]:

        return binary_search(sort, element, left, middle - 1)
    else:
        return binary_search(sort, element, middle + 1, right)
element = min(namder_2)
index = binary_search(sort, element, 0, len(sort))
print(F"последний индекс:{len(sort)-1}")
if element == max(sort):
    index_2 = index
elif element == min(sort):
    index_2 = "- не определён, так как введённое число минимальное"
else:
    index_2 = index - 1
print(f"Предшествующий числу {element} индекс:", index_2)

