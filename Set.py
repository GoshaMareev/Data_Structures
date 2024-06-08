fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
fruits.remove("banana")

other_fruits = {"kiwi", "mango"}
#Объединение
all_fruits = fruits.union(other_fruits)
# или
# all_fruits = fruits | other_fruits
print(all_fruits)

#Пересечение
intersection_fruits = fruits.intersection(other_fruits)
# или
# intersection_fruits = fruits & other_fruits


#Разность
difference_fruits = fruits.difference(other_fruits)
# или
# difference_fruits = fruits - other_fruits

#Симметрическая разность
simmetric_dif_fruits = fruits.symmetric_difference(other_fruits)
# или
# simmetric_dif_fruits = fruits ^ other_fruits