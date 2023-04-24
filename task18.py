# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9

n = int(input())
arr = list()
for i in range(n):
    a = int(input())
    arr.append(a)

x = int(input())
m = abs(x-arr[0])
number = arr[0]
for i in range(1, len(arr)):
    if m > abs(arr[i]-x):
        m = abs(arr[i]-x)
        number = arr[i]
print(number)
