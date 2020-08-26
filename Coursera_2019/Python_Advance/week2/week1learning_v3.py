# week 2 learning
# video 3. множества
"""
через сколько итераций функция random.randint(1, 10) выдаст повтор?
"""
import random


def foo(*args, **kwargs): pass

num = 100
print("Через сколько раз повторится random на числах от 1 до", num, ":")
random_set = set()  # создаем пустое множество
while True:
    new_number = random.randint(1, num)
    print(new_number, end=" ")
    if new_number in random_set:
        print()
        break
    random_set.add(new_number)
print("Ответ: через", len(random_set) + 1, "повторов")

print("-----------------------")
print(type(foo()))

