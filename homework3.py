# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих cтроках записаны N целых чисел Ai.
# Последняя строка содержит число X
# Пример: n = 5; элементы 1 2 3 4 5; x = 3; 


from random import randint

quantity = int(input("Введите количество элементов в массиве: "))

# Создадим случайный массив чисел от 0 до 9 с заданным количеством элементов:
numbers = [randint(0, 9) for num in range(quantity)]
print("Заданный массив: ", *numbers)

# Введём искомое число. Пусть оно также будет случайным в диапазоне от 0 до 9:
accidentally_num = randint(0, 9)

# Посчитаем сколько раз встречается искомое число в заданном массиве:
print(f"Вопрос: сколько раз встречается в заданном массиве число {accidentally_num}?")
count = 0
for i in numbers:
    if i == accidentally_num:
       count += 1
print(f"Ответ: -> {count}")

﻿#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

from random import randint
quantity = int(input("Введите количество элементов в массиве: "))
numbers = [randint(0, 100) for num in range(quantity)]
print("Заданный массив: ", *numbers)
accidentally_num = randint(0, 100)
print(f"Какое число в массиве является ближайшим к числу {accidentally_num} ?")
numbers = set(numbers)       
if accidentally_num in numbers:         
    numbers.remove(accidentally_num)

numbers = list(numbers)      
diff_numbers = []            

for num in numbers:
    a = abs(accidentally_num - num)    
    diff_numbers.append(a)             

min_diff = min(diff_numbers)           
ind = diff_numbers.index(min_diff)   
print(numbers[ind])                    
input("Для завершения нажмите ENTER")

