from tkinter import *
from tkinter.ttk import Combobox

def btn_click():
    mark = 0

    # Питання №1
    if v1.get() == 1 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 2
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
        mark += 1
    elif v1.get() == 0 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 1

    # Питання №2
    if v5.get() == 1:
        mark += 2

    # Питання №3
    selected_answer = combo.get()
    correct_answer = "Інтернет речей"  # Changed from "База даних"
    if selected_answer == correct_answer:
        mark += 2

    # Питання №4 (Шкала)
    mark += scale_var.get()

    # Питання №5 (Список випадаючих відповідей)
    selected_option = combo.get()  # Changed from combo_options
    if selected_option == "Інтернет речей":  # Changed from "Варіант 2"
        mark += 2

    # Питання №6 (повторення №2)
    if v6.get() == 1:
        mark += 2

    # Питання №5 (Відкрита відповідь)
    entered_answer = entry_answer.get().lower()
    correct_answer = "url"
    if entered_answer.strip() == correct_answer: 
        mark += 2

    # Відповідь
    if mark > 6:
        lbl12["fg"] = "green"  
    else:
        lbl12["fg"] = "red"  
    v7.set("Ваша оцінка: " + str(mark))

tk = Tk()
tk.title("Тест")

# шрифти, розмір тексту
font_title = ("Times New Roman.", 14, "bold")
font_q = ("Times New Roman.", 12, "bold")

# ПИТАННЯ №1 (прапорці)
lbl1 = Label(tk, text="Питання №1", font=font_title)
lbl2 = Label(tk, text="Який з пристроїв належить до пристроїв виведення даних?", font=font_q)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
chb1 = Checkbutton(tk, text="Монітор", variable=v1, onvalue=1, offvalue=0)
chb2 = Checkbutton(tk, text="Принтер", variable=v2, onvalue=1, offvalue=0)
chb3 = Checkbutton(tk, text="Колонки", variable=v3, onvalue=1, offvalue=0)
chb4 = Checkbutton(tk, text="Мишка", variable=v4, onvalue=1, offvalue=0)

# ПИТАННЯ №2 (одна правильна відповідь)
lbl3 = Label(tk, text="Питання №2", font=font_title)
lbl4 = Label(tk, text="Який пристрій належить до пристроїв введення?", font=font_q)
v5 = IntVar()
rbt1 = Radiobutton(tk, text="Сканер", variable=v5, value=1)
rbt2 = Radiobutton(tk, text="Екран", variable=v5, value=2)
rbt3 = Radiobutton(tk, text="Динамік", variable=v5, value=3)
rbt4 = Radiobutton(tk, text="Принтер", variable=v5, value=4)

# ПИТАННЯ №3 (Список випадаючих відповідей)
lbl6 = Label(tk, text="Питання №3", font=font_title)
lbl7 = Label(tk, text="Як розшифрувати ІоТ?", font=font_q)
answers = ["Інтернет телекомунікацій", "Інтернет технологій", "Інтернет речей"]
combo = Combobox(tk, values=answers)

# ПИТАННЯ №4 (Шкала)
lbl8 = Label(tk, text="Питання №4", font=font_title)
lbl8_1 = Label(tk, text="Оціни на скільки сподобався тест", font=font_q)
scale_var = IntVar()
scale = Scale(tk, from_=0, to=10, orient=HORIZONTAL, variable=scale_var)

## ПИТАННЯ №5 (Відкрита відповідь)
lbl9 = Label(tk, text="Питання №5", font=font_title)
lbl9_1 = Label(tk, text="Як скорочується *Uniform Resource Locator*?", font=font_q)
entry_answer = Entry(tk)

# ПИТАННЯ №6 (повторення №2)
lbl10 = Label(tk, text="Питання №6", font=font_title)
lbl11 = Label(tk, text="Посясни , що значить слово * HTML*", font=font_q)
v6 = IntVar()
rb_html1 = Radiobutton(tk, text="HyperText Markup Language", variable=v6, value=1)
rb_html2 = Radiobutton(tk, text="HyperText Mar Language", variable=v6, value=2)
rb_html3 = Radiobutton(tk, text="HyperText", variable=v6, value=3)

# кнопка, щоб порахувати оцінку
btn = Button(tk, text="Відповісти", command=btn_click)

# щоб оцінка виводилась в тк
v7 = StringVar()
lbl12 = Label(tk, text='', textvariable=v7)

# щоб вивелось на екрані все, що раніше прописали
lbl1.pack()
lbl2.pack()
chb1.pack()
chb2.pack()
chb3.pack()
chb4.pack()
lbl3.pack()
lbl4.pack()
rbt1.pack()
rbt2.pack()
rbt3.pack()
rbt4.pack()
lbl6.pack()
lbl7.pack()
combo.pack()
lbl8.pack()
lbl8_1.pack()
scale.pack()
lbl9.pack()
lbl9_1.pack()
entry_answer.pack()  
lbl10.pack()
lbl11.pack()
rb_html1.pack()
rb_html2.pack()
rb_html3.pack()
btn.pack()
lbl12.pack()

tk.mainloop()
