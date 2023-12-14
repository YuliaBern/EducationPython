"""Для даного числа n < 100 необхідно закінчити фразу
«На лузі пасеться…» одним з можливих продовжень: n корів, n корова,
n корови, правильно обравши закінчення. Вводиться натуральне число.
Програма повинна вивести введене число n і одне зі слів:koriv, korova або korovy.
Між числом і словом повинен стояти один пропуск.
Автор: Бернацька Юлія 31І
"""
number_animals = int(input("Введіть число n < 100: "))

# Визначення правильного закінчення слова "корова"
if  number_animals == 1:
    print(f"На лузі пасеться {number_animals} korova")
elif 2 <= number_animals  <= 4:
    print(f"На лузі пасеться {number_animals} korovy")
else:
    print(f"На лузі пасеться {number_animals} koriv")
