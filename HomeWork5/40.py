# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

text = 'AAAAAAFDDCCCCCCCAEEEEEEE'
def encode(text):
    result_text = ''
    first_char = text[0]
    count = 0
    for i in text:
        if i != first_char:
            result_text += f'{count}{first_char}'
            first_char = i
            count = 1
        else:
            count+=1
    result_text += f'{count}{first_char}'
    return result_text

def decode(text):
    result_text = ''
    count = ''
    digit = True
    for i in text:
        if digit:
            count = int(i)
            digit = False
        else:
            result_text+=int(count)*i
            digit = True
    return result_text


print(text)
print(encode(text))
encode_text = encode(text)
print(decode(encode_text))