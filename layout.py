from tkinter import *


def send(listbox,entry):
    message = entry.get()
    listbox.insert('end', message)
