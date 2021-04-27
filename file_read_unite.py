# В папке лежит некоторое количество файлов.
# Считайте, что их количество и имена вам заранее известны,
# пример для выполнения домашней работы можно взять тут
#
# Необходимо объединить их в один по следующим правилам:
#
# Содержимое исходных файлов в результирующем файле
# должно быть отсортировано по количеству строк в них
# (то есть первым нужно записать файл с наименьшим
# количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной
# информацией на 2-х строках: имя файла и количество строк в нем
# Пример Даны файлы: 1.txt
#
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
# 2.txt
#
# Строка номер 1 файла номер 2
# Итоговый файл:
#
# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1


import os

with open('1.txt', encoding='utf-8') as f:
    lines1 = f.readlines()
    # print(type(lines1))
    name1 = os.path.basename(r'C:\Users\minim\Desktop\netology\file_read_unite\1.txt')

with open('2.txt', encoding='utf-8') as f:
    lines2 = f.readlines()
    # print(type(lines2))
    name2 = os.path.basename(r'C:\Users\minim\Desktop\netology\file_read_unite\2.txt')

with open('3.txt', encoding='utf-8') as f:
    lines3 = f.readlines()
    # print(type(lines3))
    name3 = os.path.basename(r'C:\Users\minim\Desktop\netology\file_read_unite\3.txt')


full_text = []
first_list = [name1] + [len(lines1)] + lines1
second_list = [name2] + [len(lines2)] + lines2
third_list = [name3] + [len(lines3)] + lines3
full_text.append(first_list)
full_text.append(second_list)
full_text.append(third_list)


full_text.sort(key=len)
for i in range(len(full_text)):
    for k in range(len(full_text[i])):
        print(full_text[i][k])



# C:\Users\minim\Desktop\netology\file_read_unite\.git

# a = len(lines1)
# b = len(lines2)
# c = len(lines3)
# ln1 = min(a, b, c)
# ln3 = max(a, b, c)
# if a != ln1 and a != ln3:
#     ln2 = a
# elif b != ln1 and b!= ln3:
#     ln2 = b
# elif c != ln1 and c != ln3:
#     ln2 = c

# if len(lines1) == ln1:
#     print(name1)
#     print(len(lines1))
#     for i in range(len(lines1)):
#         print(lines1[i])
# elif len(lines2) == ln1:
#     print(name2)
#     print(len(lines2))
#     for i in range(len(lines2)):
#         print(lines2[i])
# elif len(lines3) == ln1:
#     print(name3)
#     print(len(lines3))
#     for i in range(len(lines3)):
#         print(lines3[i])
# if len(lines1) == ln2:
#     print(name1)
#     print(len(lines1))
#     for i in range(len(lines1)):
#         print(lines1[i])
# elif len(lines2) == ln2:
#     print(name2)
#     print(len(lines2))
#     for i in range(len(lines2)):
#         print(lines2[i])
# elif len(lines3) == ln2:
#     print(name3)
#     print(len(lines3))
#     for i in range(len(lines3)):
#         print(lines3[i])
# if len(lines1) == ln3:
#     print(name1)
#     print(len(lines1))
#     for i in range(len(lines1)):
#         print(lines1[i])
# elif len(lines2) == ln3:
#     print(name2)
#     print(len(lines2))
#     for i in range(len(lines2)):
#         print(lines2[i])
# elif len(lines3) == ln3:
#     print(name3)
#     print(len(lines3))
#     for i in range(len(lines3)):
#         print(lines3[i])
#
#



