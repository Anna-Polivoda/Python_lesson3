# slovar = {"1": "one", "2": "one"}
# print(slovar)
# slovar["privet"] = "one"
# print(slovar)
# # for item in slovar:
# #     print(item, slovar[item])
# spisok = []
# for key, value in slovar.items():
#     spisok.append([key, value])

# print(spisok)

# spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(spisok[5:2:-1])

# spisok2 = spisok[::-1] 
# print(spisok2)

# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# list_1 = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]

list_1 = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
print (list_1)
list_2 = []
for i in list_1:
    if (not i in list_2):
        list_2.append(i)
print(f'Pазличных чисел {len(list_2)}')

