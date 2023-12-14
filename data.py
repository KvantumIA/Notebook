import csv
import os
from datetime import datetime
from pathlib import Path


class Asking:
    def __init__(self):
        self.pathLib = Path("Notebook")


    def ask(self):                                  # запрос пользователя
        createNote = input("Введите название заметки: ")
        nameNote = createNote + ".csv"
        return createNote, nameNote


    def createNote(self, createNote, nameNote):         # создание заметок
        timeCreate = datetime.now()
        pathOpen = os.path.join(self.pathLib, nameNote)
        try:
            with open(pathOpen, 'w', newline='', encoding='utf-8') as file:
                createBody = input("Ввод текста: ")
                dataBody = [
                    ["Название: " + createNote],
                    ["Дата и время создания: " + timeCreate.strftime("%Y-%m-%d %H:%M:%S")],
                    ["Дата и время последнего изменения: " + timeCreate.strftime("%Y-%m-%d %H:%M:%S")],
                    ["Текст заметки: " + createBody]
                ]
                writer = csv.writer(file)
                for string in dataBody:
                    writer.writerow(string)
                print("Заметка успешно создана!")
        except FileNotFoundError:
            print(f"Файл {nameNote} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при открытии файла: {e}")


    def viewNotes(self):  # показывает какие файлы есть в папке
        try:
            fileNames = [file.name for file in self.pathLib.iterdir() if file.is_file()]
            for fileName in fileNames:
                print(fileName)
        except Exception as e:
            print(f"Произошла ошибка при открытии папки {self.pathLib}: {e}")


    def findNotes(self):            #дополнительная функция для поиска заметок
        fileNames = [file.name for file in self.pathLib.iterdir() if file.is_file()]
        notes = []
        count = 1
        for fileName in fileNames:
            print(f"{count}: {fileName}")
            count += 1
            notes.append(fileName)
        noteName = int(input("Выберите номер заметки: "))
        print()
        if noteName <= len(notes):
            return notes[noteName-1]
        else:
            print("Вы ввели неверный пункт меню. Повторите.")
            self.findNotes()


    def pathNote(self, noteName):       #Путь к файлу
        pathNote = os.path.join(self.pathLib, noteName)
        return pathNote


    def openFile(self, path):           #записывает содержимое заметки в data
        with open(path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data


    def writeFile(self, data, path):    #сделать запись в заметку
        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)


    def updateTextInFile(self):         #Заменить текст в заментке
        nameFile = self.findNotes()
        path = self.pathNote(nameFile)
        data = self.openFile(path)
        newText = input("Текст заметки: ")
        data[3][0] = "Текст заметки: " + newText
        data[2][0] = "Дата и время последнего изменения: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.writeFile(data, path)
        print("Текст успешно изменен.")


    def readFile(self):                 #Прочитать заментку
        nameFile = self.findNotes()
        path = self.pathNote(nameFile)
        data = self.openFile(path)
        for name in data:
            print(name)

    def deleteNote(self):               #Удалить заментку
        nameFile = self.findNotes()
        path = self.pathNote(nameFile)
        try:
            os.remove(path)
            print(f"Файл {nameFile} успешно удален.")
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при удалении файла: {e}")

    def updateNote(self):               #Добавить текст в заментку
        nameFile = self.findNotes()
        path = self.pathNote(nameFile)
        data = self.openFile(path)
        newText = input("Текст заметки: ")
        data[3][0] = data[3][0] + " " + newText
        data[2][0] = "Дата и время последнего изменения: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.writeFile(data, path)
        print("Текст успешно обновлен.")


    def sortNoteDate(self):
        fileList = {}
        fileNames = [file.name for file in self.pathLib.iterdir() if file.is_file()]
        for fileName in fileNames:
            path = self.pathNote(fileName)
            data = self.openFile(path)
            fileList[fileName] = data[2][0]
        print(fileList)