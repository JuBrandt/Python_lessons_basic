# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
# файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
# данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
# соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
# названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
# данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().
# ### 2. Задание на закрепление знаний по модулю json.
# # Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price),
# покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
# ### 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в
# # файле YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
# кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с помощью
# параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

# import re
# import csv
#
# def get_data():
#     global main_data
#     os_prod_list = []
#     os_name_list = []
#     os_code_list = []
#     os_type_list = []
#     main_data = []
#
#     for i in range(1,4):
#         files_names = 'info_{}.txt'.format(i)
#         file_object = open(files_names)
#         data = file_object.read()
#
#         # Получаем список изготовителей системы
#         os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
#         os_prod_mas = os_prod_reg.findall(data)
#         os_prod_list.append(os_prod_mas[0].split()[2])
#
#         # Название ОС
#         os_name_reg = re.compile(r'Windows\s\S*')
#         os_name_mas = os_name_reg.findall(data)
#         os_name_list.append(os_name_mas[0])
#
#         # Код продукта
#         os_code_reg = re.compile(r'Код продукта:\s*\S*')
#         os_code_mas = os_code_reg.findall(data)
#         os_code_list.append(os_code_mas[0].split()[2])
#
#         # Тип системы
#         os_type_reg = re.compile(r'Тип системы:\s*\S*')
#         os_type_mas = os_type_reg.findall(data)
#         os_type_list.append(os_type_mas[0].split()[2])
#
#     headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
#     main_data.append(headers)
#
#     j = 1
#     for i in range(0, 3):
#         row_data = []
#         row_data.append(j)
#         row_data.append(os_prod_list[i])
#         row_data.append(os_name_list[i])
#         row_data.append(os_code_list[i])
#         row_data.append(os_type_list[i])
#         main_data.append(row_data)
#         j = j + 1
#
#
# def write_to_csv(out_file):
#     get_data()
#     with open(out_file, 'w') as f:
#         writer = csv.writer(f)
#         for row in main_data:
#             writer.writerow(row)
#
#
# out_file = 'data_report.csv'
# write_to_csv(out_file)


# import json
#
# def write_order_to_json(item, quantity, price, buyer, date):
#     with open('orders.json', 'r') as file_out:
#         data = json.load(file_out)
#     with open('orders.json', 'w') as file_in:
#         check_list = data['orders']
#         check_info = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
#         check_list.append(check_info)
#         json.dump(data, file_in, indent = 4)
#         print(data)
#
# write_order_to_json('videoplayer', '1', '7900', 'Petrov A.A.', '06.10.2018')

import yaml

data_input = {'items': ['notebook', 'powerbank', 'wifi-router', 'mouse'],
        'items_quantity': 4,
        'items_ptice': {'notebook': '200€-1000€',
                       'powerbank': '100€-300€',
                       'wifi-router': '5€-50€',
                       'mouse': '4€-7€'}
        }

with open('file.yaml', 'w', encoding='utf-8') as file_in:
    yaml.dump(data_input, file_in, default_flow_style=False, allow_unicode=True)

with open("file.yaml", 'r', encoding='utf-8') as file_out:
    data_out = yaml.load(file_out)

print(data_input == data_output)
