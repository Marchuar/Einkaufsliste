from tkinter import *
import json
import os
import random
import webbrowser

# Сохраняем оригинальные тексты элементов
original_texts = {}

# Переменная для отслеживания текущей темы
dark_mode = False

# Цветовая схема
light_colors = {
    'bg': 'SystemButtonFace',
    'fg': 'black',
    'button_bg': 'SystemButtonFace',
    'button_fg': 'black',
    'listbox_bg': 'white',
    'listbox_fg': 'black'
}

dark_colors = {
    'bg': '#2b2b2b',
    'fg': '#ffffff',
    'button_bg': '#3d3d3d',
    'button_fg': '#ffffff',
    'listbox_bg': '#1e1e1e',
    'listbox_fg': '#ffffff'
}

def shuffle_text(text):
    """Перемешивает буквы в тексте"""
    if not text:
        return text
    chars = list(text)
    random.shuffle(chars)
    return ''.join(chars)

def toggle_dark_mode():
    """Переключает между светлой и тёмной темой"""
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()
    disco_effect()

def apply_theme():
    """Применяет выбранную тему к элементам интерфейса"""
    colors = dark_colors if dark_mode else light_colors

    fenster.configure(bg=colors['bg'])
    Kauf_label.config(bg=colors['bg'], fg=colors['fg'])
    eingabefeld1.config(bg=colors['listbox_bg'], fg=colors['listbox_fg'], insertbackground=colors['listbox_fg'])
    Hinzufugen_button.config(bg=colors['button_bg'], fg=colors['button_fg'])
    ausgabefeld.config(bg=colors['listbox_bg'], fg=colors['listbox_fg'])
    Speichern_button.config(bg=colors['button_bg'], fg=colors['button_fg'])
    Laden_button.config(bg=colors['button_bg'], fg=colors['button_fg'])
    Loschen_button.config(bg=colors['button_bg'], fg=colors['button_fg'])
    Rickroll_button.config(bg=colors['button_bg'], fg=colors['button_fg'])
    DarkMode_checkbox.config(bg=colors['bg'], fg=colors['fg'], selectcolor=colors['bg'])

def disco_effect():
    """Эффект дискотеки: яркие цвета, ритмичная музыка и перемешивание букв"""
    colors = ['red', 'cyan', 'yellow', 'magenta', 'lime', 'orange', 'purple', 'blue']
    frequencies = [800, 1200, 600, 1000, 800, 1200]  # Ритмичные частоты

    def animate_disco(frame=0):
        if frame < len(colors) * 2:  # Дискотека в течение 16 кадров
            # Визуальный эффект - смена цветов
            color = colors[frame % len(colors)]
            fenster.configure(bg=color)

            # Эффект перемешивания букв
            Kauf_label.config(text=shuffle_text(original_texts['label']))
            count_label.config(text=shuffle_text(original_texts['count']))
            Hinzufugen_button.config(text=shuffle_text(original_texts['hinzufugen']))
            Speichern_button.config(text=shuffle_text(original_texts['speichern']))
            Laden_button.config(text=shuffle_text(original_texts['laden']))
            Loschen_button.config(text=shuffle_text(original_texts['loschen']))
            Rickroll_button.config(text=shuffle_text(original_texts['rickroll']))

            fenster.update()

            # Следующий кадр через 100ms
            fenster.after(100, lambda: animate_disco(frame + 1))
        else:
            # Возврат к нормальному цвету и текстам
            apply_theme()
            fenster.configure(bg='SystemButtonFace')
            Kauf_label.config(text=original_texts['label'])
            count_label.config(text=original_texts['count'])
            Hinzufugen_button.config(text=original_texts['hinzufugen'])
            Speichern_button.config(text=original_texts['speichern'])
            Laden_button.config(text=original_texts['laden'])
            Loschen_button.config(text=original_texts['loschen'])
            Rickroll_button.config(text=original_texts['rickroll'])

    animate_disco()

def update_count():
    """Обновляет текст метки с количеством элементов"""
    count = ausgabefeld.size()
    text = f"Items: {count}"
    count_label.config(text=text)
    original_texts['count'] = text

def hinzufugen():
  Artikel = eingabefeld1.get()
  if Artikel:  # Проверка, что поле не пусто
    ausgabefeld.insert(END, Artikel)
    eingabefeld1.delete(0, END)
    update_count()
    disco_effect()

def speichern():
    Artikeln = list(ausgabefeld.get(0, END))
    try:
        with open('liste.json', 'w', encoding='utf-8') as datei:
            json.dump(Artikeln, datei, ensure_ascii=False, indent=2)
        print("Список сохранён в liste.json")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def laden():
    try:
        if os.path.exists('liste.json'):
            with open('liste.json', 'r', encoding='utf-8') as datei:
                Artikeln = json.load(datei)
            ausgabefeld.delete(0, END)
            for artikel in Artikeln:
                ausgabefeld.insert(END, artikel)
            update_count()
            print("Список загружен из liste.json")
        else:
            print("Файл liste.json не найден")
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")

def loschen():
    selected = ausgabefeld.curselection()
    if selected:
        ausgabefeld.delete(selected[0])
        update_count()

def rickroll():
    """Открывает рикролл в браузере"""
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")






fenster = Tk()
fenster.title("Einkaufsliste")

Kauf_label = Label(fenster, text = "Auf die Einkaufsliste: ")
count_label = Label(fenster, text = "Items: 0")
eingabefeld1 = Entry(fenster, bd=5, width = 50)
Hinzufugen_button = Button(fenster, text = "Hinzufügen", command=hinzufugen)
ausgabefeld = Listbox(fenster, bd=5, width=50, height=5)
Speichern_button = Button(fenster, text = "Speichern", command=speichern)
Laden_button = Button(fenster, text = "Laden", command=laden)
Loschen_button = Button(fenster, text = "Löschen", command=loschen)
Rickroll_button = Button(fenster, text = "сиси", command=rickroll)
DarkMode_checkbox = Checkbutton(fenster, text="Тёмная тема", command=toggle_dark_mode)

# Сохраняем оригинальные тексты
original_texts['label'] = "Auf die Einkaufsliste: "
original_texts['count'] = "Items: 0"
original_texts['hinzufugen'] = "Hinzufügen"
original_texts['speichern'] = "Speichern"
original_texts['laden'] = "Laden"
original_texts['loschen'] = "Löschen"
original_texts['rickroll'] = "сиси"

Kauf_label.grid(row=1, column=0)
eingabefeld1.grid(row=1, column=1)
Hinzufugen_button.grid(row=2, column=0)
Speichern_button.grid(row=3, column=0)
Laden_button.grid(row=4, column=0)
Loschen_button.grid(row=5, column=0)
Rickroll_button.grid(row=6, column=0)
DarkMode_checkbox.grid(row=7, column=0)
ausgabefeld.grid(row=3, column=1, rowspan=3)
count_label.grid(row=2, column=1)

apply_theme()

mainloop()