# Словарь

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)

# Доступ к значению по ключу
print(person["name"])

#len()
print(len(person))
# Изменение значения
person["age"] = 31
print(person)

# Добавление новой пары ключ-значение
person["email"] = "john@example.com"
print(person)

# Удаление пары ключ-значение
# del person["city"]
# print(person)

# Удаление и возвращение значения
# p = person.pop("city")
# print(person)
# print(p)

# Итерация по словарю
# for key in person:
#     print(key, person[key])
# # # или
# for key, value in person.items():
#      print(key, value)

# Получение всех ключей и значений
# keys = person.keys()
# values = person.values()
# items = person.items()
# print(keys)
# print(values)
# print(items)

# Пример
# Сколько раз встречается символ в строке
# s = "Hello! How's it going?"
# dictionary = {i: s.count(i) for i in set(s)}
# print(dictionary)

# #zip
# s1 = [1, 2, 3, 4]
# s2 = ["один", "два", "три", "четыре"]
# dict2 = dict(zip(s1, s2))
# print(dict2)

# if  "age" in person.keys(): # in person метод keys используется по умолчанию
#     print("Данный ключ уже используется")
# else:
#     print("Можно использовать данный ключ")

# Пример Favorite meal

# Пример словарь словарей
# workers = {
#     "John":{
#         "age": 30,
#         "city": "New York"
#     }
# }
# Вывод cловаря словарей
# for worker_name, worker_info in workers.items():
#     print(f'Worker name: {worker_name}')
#     worker_age = worker_info["age"]
#     worker_city = worker_info["city"]
#     print(f'Worker  {worker_name} age:{worker_age}  ')
#     print(f"Worker  {worker_name} city:{worker_city}  ")
#или
# for i in workers.keys():
#     for key, value in workers[i].items():
#         print(key, value)
# Методы
# dict.get(key, default=None): Возвращает значение для key, если ключ существует,
# иначе default.
# print(person.get("name"))
# print(person.get("country", "Wtf?"))
#
# dict.setdefault(key, default=None): Возвращает значение для key, если ключ существует.
# Если ключ не существует, вставляет key с default и возвращает default.
# print(person.setdefault("country", 'USA'))
# print(person)

#dict.pop(key, default=None): Удаляет ключ и возвращает его значение.
# Если ключ не найден, возвращает default.
# my_dict = {'a': 1, 'b': 2}
# print(my_dict.pop('a'))  # 1
# print(my_dict)  # {'b': 2}

#dict.popitem(): Удаляет и возвращает последнюю пару (ключ, значение) из словаря.
# Если словарь пуст, вызывает ошибку.
# my_dict = {'a': 1, 'b': 2}
# print(my_dict.popitem())  # ('b', 2)
# print(my_dict)  # {'a': 1}


# update() dict.update([other]): Обновляет словарь, добавляя пары (ключ, значение) из other.
# Существующие ключи будут обновлены.
# my_dict = {'a': 1}
# my_dict2 = {'b': 2, 'a': 3}
# my_dict.update(my_dict2)
# print(my_dict) #{'a': 3, 'b': 2}

#Сортировка словаря по ключам
# print(dict(sorted(person.items())))
# sorted_by_keys = {k: person[k] for k in sorted(person)}
# print(sorted_by_keys)
