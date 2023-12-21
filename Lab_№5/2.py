"""
2.У вхідному файлі записаний текст. Словом вважається послідовність
непробільних символів, що йдуть підряд, слова розділені одним або
більшим числом пропусків або символами кінця рядка. Визначте, скільки різних
слів міститься в цьому тексті.
Автор: Бернацька Юлія 31І
"""
with open('input.txt', 'r') as file:
       lines = file.readlines()
words_count = {}

for line in lines:
       for word in line.split():
              if word not in words_count:
                   words_count[word] = 1
              else:
                   words_count[word] += 1

finish_words = len(words_count)

print(f"Кількість різних слів у тексті: {finish_words}")
