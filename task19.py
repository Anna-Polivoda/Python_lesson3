# 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 3
# 7 8 9 1 2 3 4 5 6

arr=[1, 2, 3, 4, 5, 6, 7, 8, 9]
k=3
arr2=arr[-k:] + arr[:-k]
print(arr2)


