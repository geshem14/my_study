# week 2 learning
# video 2. dictionaries
"""
найти 3 самых часто встречающихся слова в Zen of Python
"""
import operator
import collections

zen = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
zen_map = dict()
for word in zen.split():
    cleaned_word = word.strip('.,!-*').lower()
    # очищаем нашу строку от спецсимволов и приводим к нижнему регистру
    if cleaned_word not in zen_map:  # если слова ещё нет в zen_map:
        zen_map[cleaned_word] = 0  # добавляем ключ
    zen_map[cleaned_word] += 1
# print(zen_map)

zen_items = zen_map.items()  # список кортежей (ключ, значение)
# с помощью метода items().
word_count_items = sorted(zen_items, key=operator.itemgetter(1), reverse=True)
# отсортируем список по вторым элементам в кортеже, используя модуль operator.
# В метод sorted() в качестве аргумента key передадим operator.itemgetter(1)
print("3 самых часто встречающихся слова в Zen of Python:")
for i in range(3):
    print("\"", word_count_items[i][0], "\" встречается ",
          word_count_items[i][1], " раз;", sep="")

# проверка результата с помощью метода Counter из модуля collections
cleaned_list = []
for word in zen.split():
    cleaned_list.append(word.strip('.,-!').lower())
print("проверка результата с помощью метода Counter из модуля collections:")
print(collections.Counter(cleaned_list).most_common(3))
