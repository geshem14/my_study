# week 2 learning
# video 1. Lists and Tuples
"""
поиск медианы случайного списка. Медиана - это значение в отсортированном
списке, которое лежит ровно посередине, таким образом, половина значений -
слева от него, и половина значений --- справа
"""
import random
import statistics

numbers = []
numbers_size = random.randint(10, 15)
print("Size of list:", numbers_size)  # напечатаем размер списка
# мы не будем использовать переменную, которую используем
# для итерации, поэтому назовём её _
for _ in range(numbers_size):
    numbers.append(random.randint(10, 20))
    # randint возвращает случайное целое
    # число в переданном ей интервале
print(numbers)  # напечатаем список

numbers.sort()  # отсортируем список изменяя его
print("Отсортированный список:")
print(numbers)  # напечатаем отсортированный список

half_size = len(numbers) // 2
median = None
if numbers_size % 2 == 1:
    median = numbers[half_size]
else:
    median = sum(numbers[half_size - 1:half_size + 1]) / 2
numbers.sort()

print("Медиана:", median)
print("Проверка ответа с помощью метода медиана:", statistics.median(numbers))
