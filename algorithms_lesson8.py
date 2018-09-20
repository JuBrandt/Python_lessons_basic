# 2. Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

import hashlib

print(hashlib.sha3_256(b'www.geekbrains.ru').hexdigest())

s = hashlib.sha1(b'www.geekbrains.ru').hexdigest()

print(hashlib.sha1(b'www.geekbrains.ru' + bytes(s.encode('utf-8'))).hexdigest())
