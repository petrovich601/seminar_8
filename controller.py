# 1. Какой класс? открываем конкретный файл
# 2. Какой предмет?
#     3. Показывает весь список учеников и их оценки по предмету
#     4. Вызвать к доске? если ввести exit то выходит из программы
#     5. На какую оценку ответ?
# 6. После выхода сохранить все изменения в текущий файл

import view
import model

def start():
    model.set_class(view.input_class())
    model.set_subject(view.input_subject())
    model.open_file()
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == 'exit' or student == '':
            break
        mark = int(view.what_mark())
        model.student_mark(student, mark)
    model.save_file()