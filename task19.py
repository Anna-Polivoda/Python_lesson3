# 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 3
# 7 8 9 1 2 3 4 5 6

arr=[1, 2, 3, 4, 5, 6, 7, 8, 9]
k=3
arr2=arr[-k:] + arr[:-k]
print(arr2)






# my_dict = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": " S005 ", " V ":" S009 ", " VIII ":" S007 ", "IV":"holla", "1234": "S005"}

# values = list(my_dict.values())
# unique_values = set(values)

# print("Уникальные значения в словаре:")
# for value in unique_values:
#     print(value)


# #задача 21

# test_list = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": " S005 ", " V ":" S009 ", " VIII ":" S007 ", "IV":"holla", "1234": "S005"}
# #res = list(set(val for dic in test_list for val in dic.values()))
# a = []

# for value in test_list.values():
#      a.append(value)
# a = set(a)


# print(a)





# вторая задача: list_1 = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(list_1)):
#     if list_1[i] > list_1[i-1]:
#         count += 1
# print(count)



# #Задача 23

# arr = [0, -1, 5, 2, 3, 4, 0]
# count = 0

# for x in range(1, len(arr)):
#     if arr[x - 1] < arr[x]:
#         count += 1

# print(count)

 