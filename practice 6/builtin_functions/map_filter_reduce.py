from functools import reduce

# map — применяет функцию ко всем элементам
numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)


# filter — фильтрует по условию
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# reduce — сворачивает список в одно значение
sum_all = reduce(lambda x, y: x + y, numbers)
print("Sum:", sum_all)