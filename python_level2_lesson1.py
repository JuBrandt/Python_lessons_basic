# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
# # # проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера
# # # преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.


# string_dev = 'разработка'
# string_socket = 'сокет'
# string_dec = 'декоратор'
# print(string_socket, string_dev, string_dec)
# print(type(string_dec), type(string_dev), type(string_socket))
# print(string_dev.encode('utf-8'))
# encode_string_dev = string_dev.encode('utf-8')
# encode_string_socket = string_socket.encode('utf-8')
# encode_string_dec = string_dec.encode('utf-8')
# print(type(encode_string_dev), type(encode_string_socket), type(encode_string_dec))
# print(encode_string_dev)
# print(encode_string_dec.decode('utf-8'), encode_string_socket.decode('utf-8'), encode_string_dev.decode('utf-8'))


# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
# последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и
# длину соответствующих переменных.

import pickle


s = 'class'
m = 'function'
d = 'method'
s_encode = pickle._dumps(s)
m_encode = pickle._dumps(m)
d_encode = pickle._dumps(d)

print(s_encode)
print(m_encode)
print(d_encode)
print('*' * 50)
print(len(s), type(s), type(s_encode), len(s_encode))
print(len(m), type(m), type(m_encode), len(m_encode))
print(len(d), type(d), type(d_encode), len(d_encode))

print('*' * 50)
print(pickle._loads(s_encode))
print(pickle._loads(m_encode))
print(pickle._loads(d_encode))

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

# string_attr = 'attribute'
# string_class = 'класс'
# string_func = 'функция'
# string_type = 'type'
# print(string_attr.encode('utf-8'), string_class.encode('utf-8'), string_func.encode('utf-8'), string_type.encode('utf-8'), sep='----')

# attribute, type невозможно записать в байтовом типе


# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
# представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).


# string_dev = 'разработка'
# string_admin = 'администрирование'
# string_protocol = 'protocol'
# string_standart = 'standart'
# encode_string_dev = string_dev.encode('utf-8')
# encode_string_admin = string_admin.encode('utf-8')
# encode_string_protocol = string_protocol.encode('utf-8')
# encode_string_standart = string_standart.encode('utf-8')
# print(encode_string_dev, encode_string_admin, encode_string_protocol, encode_string_standart, sep='---')
# print(encode_string_dev.decode('utf-8'), encode_string_admin.decode('utf-8'), encode_string_protocol.decode('utf-8'), encode_string_standart.decode('utf-8'))

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

# import subprocess
#
# args_p = ['ping', 'yandex.ru']
# args_y = ['ping', 'youtube.com']
# subproc_ping = subprocess.Popen(args_p, stdout=subprocess.PIPE)
#
# for line in subproc_ping.stdout:
#     line = line.decode('cp866').encode('utf-8')
#     print(line.decode('utf-8'))
#
# subproc_ping_y = subprocess.Popen(args_y, stdout=subprocess.PIPE)
#
# for line_y in subproc_ping_y.stdout:
#     line_y = line_y.decode('cp866').encode('utf-8')
#     print(line_y.decode('utf-8'))
#
# args_m = ['ping', 'mail.ru']
# subproc_ping_m = subprocess.Popen(args_m, stdout=subprocess.PIPE)
#
# for line_m in subproc_ping_m.stdout:
#     line_m = line_m.decode('cp866').encode('utf-8')
#     print(line_m.decode('utf-8'))




# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.


# write_text = open('text_file.txt', 'w', encoding='utf-8')
# write_text.write('сетевое программирование\nсокет\nдекоратор')
# write_text.close()
# with open(r'text_file.txt', 'r', encoding='utf-8') as write_text:
#     for i in write_text:
#         print(i)


