# week 2 task 18
"""
текст задания
Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂.
Определите, можно ли разместить одну из этих коробок внутри другой,
при условии, что поворачивать коробки можно только на 90 градусов
вокруг ребер.
Формат вывода
Программа должна вывести одну из следующих строчек:
Boxes are equal, если коробки одинаковые,
The first box is smaller than the second one,
если первая коробка может быть положена во вторую,
The first box is larger than the second one,
если вторая коробка может быть положена в первую,
Boxes are incomparable, во всех остальных случаях.
"""
a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
"""
1. первым шагом отсортируем стороны первой коробки по возрастанию
"""
if a1 <= c1 <= b1:
    (b1, c1) = (c1, b1)
elif b1 <= a1 <= c1:
    (a1, b1) = (b1, a1)
elif c1 <= a1 <= b1:
    (a1, b1, c1) = (c1, a1, b1)
elif c1 <= b1 <= a1:
    (a1, c1) = (c1, a1)
elif b1 <= c1 <= a1:
    (a1, b1, c1) = (b1, c1, a1)
# теперь стороны первой коробки отсортированы
"""
2. вторым шагом отсортируем стороны второй коробки по возрастанию
"""
if a2 <= c2 <= b2:
    (b2, c2) = (c2, b2)
elif b2 <= a2 <= c2:
    (a2, b2) = (b2, a2)
elif c2 <= a2 <= b2:
    (a2, b2, c2) = (c2, a2, b2)
elif c2 <= b2 <= a2:
    (a2, c2) = (c2, a2)
elif b2 <= c2 <= a2:
    (a2, b2, c2) = (b2, c2, a2)
"""
3.третьим шагом сравниваем коробки и если они равны тогда пишем что они равны
и если больше или меньше аналогично пишем результат
"""
if (a1 == a2) and (b1 == b2) and (c1 == c2):
    print("Boxes are equal")
elif (a1 <= a2) and (b1 <= b2) and (c1 <= c2):
    print("The first box is smaller than the second one")
elif (a1 >= a2) and (b1 >= b2) and (c1 >= c2):
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
