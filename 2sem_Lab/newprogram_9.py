#Напишіть програму, яка реалізує класичний алгоритм
#сортування рядків двовимірного масиву методом обміну
#Розмірність масиву та всі елементи генеруються за допомогою випадкових чисел.
#Автор: Бернацька Юлія 31І група


import random


# Генерує двовимірний масив з випадкових чисел
def generate_random_matrix(rows, cols, min_val=0, max_val=100):
    matrix = []
    for _ in range(rows):
        row = [random.randint(min_val, max_val) for _ in range(cols)]
        matrix.append(row)
    return matrix

# Виводить матрицю на екран
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Сортує рядки двовимірного масиву 
def bubble_sort_matrix_rows(matrix):
    for row in matrix:
        n = len(row)
        for i in range(n):
            for j in range(0, n - i - 1):
                if row[j] > row[j + 1]:
                    row[j], row[j + 1] = row[j + 1], row[j]


def main():
    # Встановлюємо розміри матриці
    rows = 5  
    cols = 5  

    # Генеруємо випадкову матрицю
    matrix = generate_random_matrix(rows, cols)

    print("Початкова матриця:")
    print_matrix(matrix)

    # Сортуємо рядки матриці методом обміну
    bubble_sort_matrix_rows(matrix)

    print("\nМатриця після сортування рядків:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()
