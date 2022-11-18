try:
    subsequence = input("Введите последовательность чисел через пробел: ").split()
    num = int(input("Введите целое число: "))
    num_list = [int(i) for i in subsequence]
    num_list.sort()
    print(f"Преобразование в список: {type(num_list)}")
    print(f"Сортировка списка по возрастанию: {num_list}")
except ValueError:
    print("Неверный ввод!")
else:
    def index_search_min(num_list, num):
        left = -1
        right = len(num_list)
        while right > left + 1:
            middle = (left + right) // 2
            if num_list[middle] >= num:
                right = middle
            else:
                left = middle
        return left
    def index_search_max(num_list, num):
        left = -1
        right = len(num_list)
        while right > left + 1:
            middle = (left + right) // 2
            if num_list[middle] >= num:
                right = middle
            else:
                left = middle
        return right
    if num < min(num_list):
        print(f"Числа меньше введенного нет, индекс числа больше или равно введенному: {index_search_max(num_list, num)}")
    elif num > max(num_list):
        print(f"Индекс числа меньше введенного: {index_search_min(num_list, num)}, числа больше введенного нет")
    else:
        print(f"Индекс числа меньше введенного: {index_search_min(num_list, num)}, индекс числа больше или равно введенному: {index_search_max(num_list, num)}")
