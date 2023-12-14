from data import Asking


# controller = Asking()
class Start:
    def __init__(self):
        self.controller = Asking()

    def start(self):
        print()
        print("Выберите пункт меню:\n"
              "1. Создать заметку.\n"
              "2. Заменить текст заметки.\n"
              "3. Добавить текст в заметку.\n"
              "4. Просмотреть список заметок.\n"
              "5. Прочитать заметку.\n"
              "6. Удалить заметку.\n"
              "7. Отсортировать по дате изменения. \n"
              "8. Отсортировать по дате создания.\n"
              "9. Выход.")
        num = int(input("Ввод: "))
        print()

        if num == 1:
            createNote, findNote = self.controller.ask()
            self.controller.createNote(createNote, findNote)
            self.stop()
        elif num == 2:
            self.controller.updateTextInFile()
            self.stop()
        elif num == 3:
            self.controller.updateNote()
            self.stop()
        elif num == 4:
            self.controller.viewNotes()
            self.stop()
        elif num == 5:
            self.controller.readFile()
            self.stop()
        elif num == 6:
            self.controller.deleteNote()
            self.stop()
        elif num == 7:
            self.controller.sortNoteDate()
            self.stop()
        elif num == 8:
            self.controller.sortNoteDateCreate()
            self.stop()
        elif num == 9:
            SystemExit
        else:
            print("Вы неверно ввели пункт меню. Повторите ввод.")
            self.start()

    def stop(self):
        print()
        print("1. Назад в меню.\n"
              "2. Выход из программы.")
        num = int(input("Ввод: "))
        if num == 1:
            self.start()
        elif num == 2:
            SystemExit
        else:
            print("Вы неверно ввели пункт меню. Повторите ввод.")
            self.stop()