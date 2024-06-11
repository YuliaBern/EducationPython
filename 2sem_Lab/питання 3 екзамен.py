#Питання №3
#Виконала студентка 31І групи
#Бернацька Юлія

b = 0
c = 1
m_index = 0
while True:
    n = int(input())
    if n != 0:
        if n == b:
            c += 1
        if b < n:
           c = 1
           b = n
    else:
        break
print(c)