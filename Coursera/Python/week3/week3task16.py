# week 3 task 16
"""
текст задания                                                 тут 79 символ=>!
Дана строка, в которой буква h встречается минимум два раза.Удалите из этой
строки первое и последнее вхождение буквы h,
а также все символы, находящиеся между ними.
"""
string = input()  # строковая переменная для ввода
search_string = "h"  # искомая строка
position1 = string.find(search_string)  # переменная для первой позиции входа
position_last = string.rfind(search_string)
# переменная для последней позиции входа
print(string[:position1]+string[position_last+1:])
