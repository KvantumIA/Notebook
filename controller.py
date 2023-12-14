from data import Asking

controller = Asking()
createNote, findNote = controller.ask()
controller.createNotebook(createNote, findNote)
