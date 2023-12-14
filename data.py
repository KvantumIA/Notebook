import csv
import os
from datetime import datetime
from pathlib import Path

class Asking:
    def __init__(self):
        self.pathLib = Path("Notebook")
        # self.createNote = createNote
        # self.findNote = findNote


    def ask(self):
        createNote = input("Введите название заметки: ")
        findNote = createNote + ".csv"
        return createNote, findNote


    def createNotebook(self, createNote, findNote):
        timeCreate = datetime.now()
        pathOpen = os.path.join(self.pathLib, findNote)
        with open(pathOpen, 'w', newline='', encoding='utf-8') as file:
            createBody = input("Ввод текста: ")
            fails = self.pathLib.iterdir()
            findFile = any(self.pathLib.name == findNote for file in fails)
            if findFile:
                infoFile = os.stat(createNote)
                infoFileTime = infoFile.st_mtime
                dataBody = [
                    ["Название: " + createNote],
                    ["Дата и время создания: " + timeCreate.strftime("%Y-%m-%d %H:%M:%S")],
                    ["Дата и время последнего изменения: " + datetime.fromtimestamp(infoFileTime)],
                    ["Текст заметки: " + createBody]
                ]
            else:
                dataBody = [
                    ["Название: " + createNote],
                    ["Дата и время создания: " + timeCreate.strftime("%Y-%m-%d %H:%M:%S")],
                    ["Дата и время последнего изменения: " + timeCreate.strftime("%Y-%m-%d %H:%M:%S")],
                    ["Текст заметки: " + createBody]
                ]
            writer = csv.writer(file)
            for string in dataBody:
                writer.writerow(string)

    def correctNote(self, createNote, findNote):
        timeCreate = datetime.now()
        pathOpen = os.path.join(self.pathLib, findNote)
        with open(pathOpen, 'w', newline='', encoding='utf-8') as file:
            createBody = input("Ввод текста: ")
            fails = self.pathLib.iterdir()
            findFile = any(self.pathLib.name == findNote for file in fails)
            if findFile:
                infoFile = os.stat(createNote)
                infoFileTime = infoFile.st_mtime
                dataBody = [
                    ["Название: " + createNote],
                    ["Дата и время создания: " + timeCreate.strftime("%Y-%m-%d %H:%M:%S")],
                    ["Дата и время последнего изменения: " + datetime.fromtimestamp(infoFileTime)],
                    ["Текст заметки: " + createBody]
                ]
            else:
                dataBody = [
                    ["Название: " + createNote],
                    ["Дата и время создания: " + timeCreate.strftime("%Y-%m-%d %H:%M:%S")],
                    ["Дата и время последнего изменения: " + timeCreate.strftime("%Y-%m-%d %H:%M:%S")],
                    ["Текст заметки: " + createBody]
                ]
            writer = csv.writer(file)
            for string in dataBody:
                writer.writerow(string)