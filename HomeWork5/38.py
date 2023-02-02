# Напишите программу, удаляющую из текста все слова, 
# содержащие ""абв"".(Задание из семинара)

text = "Привет, меабв! ааааа вабв, ааа! Вабв, абв"
text = text.split()
text_new = list(filter(lambda x: True if 'абв' not in x else False, text))
print(" ".join(text_new))