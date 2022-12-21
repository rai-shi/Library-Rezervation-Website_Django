from tkinter import *
from tkinter.font import Font
from tkinter import ttk 

from PIL import ImageTk
import PIL.Image

def openLibEntryState(canvas_list:list):
    canvas_list[0].place_forget()
    canvas_list[1].place(relx=.5, rely=.5,anchor= CENTER)

def openLibExitState(canvas_list:list):
    canvas_list[0].place_forget()
    canvas_list[2].place(relx=.5, rely=.5,anchor= CENTER)


def openLibTakeBreakState(canvas_list:list):
    canvas_list[0].place_forget()
    canvas_list[3].place(relx=.5, rely=.5,anchor= CENTER)

def openLibReturnBreakState(canvas_list:list):
    canvas_list[0].place_forget()
    canvas_list[4].place(relx=.5, rely=.5,anchor= CENTER)



def EntryState_returnHomePage(canvas_list:list):
    canvas_list[0].place(relx=.5, rely=.5,anchor= CENTER)
    canvas_list[1].place_forget()

def ExitState_returnHomePage(canvas_list:list):
    canvas_list[0].place(relx=.5, rely=.5,anchor= CENTER)
    canvas_list[2].place_forget()

def TakeBreakState_returnHomePage(canvas_list:list):
    canvas_list[0].place(relx=.5, rely=.5,anchor= CENTER)
    canvas_list[3].place_forget()

def ReturnBreakState_returnHomePage(canvas_list:list):
    canvas_list[0].place(relx=.5, rely=.5,anchor= CENTER)
    canvas_list[4].place_forget()


def lib_Enter():
    pass


def lib_Exit():
    pass


def lib_TakeBreak():
    pass


def lib_ReturnBreak():
    pass