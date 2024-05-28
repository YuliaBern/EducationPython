#2.Дані початок та кінець n робіт. Знайти максимальну кількість робіт, які
#можна виконати, якщо в один момент часу можна виконувати тільки одну роботу.
#Автор: Бернацька Юлія - студентка 31І групи

def max_activities(start, end):
    # Об'єднуємо початок і кінець у список пар (start[i], end[i])
    activities = list(zip(start, end))
    # Сортуємо список за часом завершення робіт
    activities.sort(key=lambda x: x[1])
    
    
    count = 1
    last_end_time = activities[0][1]
    
    # Вибираємо роботи, які не перекриваються з обраними
    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            count += 1
            last_end_time = activities[i][1]
    
    return count

# Приклад використання функції
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

print("Максимальна кількість робіт, які можна виконати:", max_activities(start, end))
