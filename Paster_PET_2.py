from tkinter import *
from tkcalendar import Calendar, DateEntry
import matplotlib
import matplotlib.pyplot as plt
from tkinter.tix import *
import sqlite3
from PIL import Image, ImageTk

def plot():
    day = str(date.get())
    x = []
    y = []
    z = []
    w = []
    v = []
    k = []

    top = Toplevel(root)
    top.title('Легенда')
    top.geometry('350x170')
    image_open = Image.open('legend.png')
    img = ImageTk.PhotoImage(image_open)
    Label(top, image = img).place(x = 0, y = 0)
    
    with sqlite3.connect("database.db") as db:
        
        cursor_time = db.cursor()
        query_time = """SELECT time
                FROM Paster_PET_2
                WHERE (date = '%(day)s')
                """ %{'day' : day}
        cursor_time.execute(query_time)
        for i in cursor_time.execute(query_time):
            string = str(i)
            string = string.replace("('", '')
            string = string.replace("',)", '')
            x.append(string)

        cursor_flow = db.cursor()
        query_flow = """SELECT flow
                FROM Paster_PET_2
                WHERE (date = '%(day)s')
                """ %{'day' : day}
        cursor_flow.execute(query_flow)
        for i in cursor_flow.execute(query_flow):
            string = str(i)
            string = string.replace("('", '')
            string = string.replace("',)", '')
            string = float(string)
            y.append(string)

        cursor_PU = db.cursor()
        query_PU = """SELECT PU
                FROM Paster_PET_2
                WHERE (date = '%(day)s')
                """ %{'day' : day}
        cursor_PU.execute(query_PU)
        for i in cursor_PU.execute(query_PU):
            string = str(i)
            string = string.replace("('", '')
            string = string.replace("',)", '')
            string = float(string)
            z.append(string)

        cursor_temp_past = db.cursor()
        query_temp_past = """SELECT temp_past
                FROM Paster_PET_2
                WHERE (date = '%(day)s')
                """ %{'day' : day}
        cursor_temp_past.execute(query_temp_past)
        for i in cursor_temp_past.execute(query_temp_past):
            string = str(i)
            string = string.replace("('", '')
            string = string.replace("',)", '')
            string = float(string)
            w.append(string)

        cursor_temp_cool = db.cursor()
        query_temp_cool = """SELECT temp_cool
                FROM Paster_PET_2
                WHERE (date = '%(day)s')
                """ %{'day' : day}
        cursor_temp_cool.execute(query_temp_cool)
        for i in cursor_temp_cool.execute(query_temp_cool):
            string = str(i)
            string = string.replace("('", '')
            string = string.replace("',)", '')
            string = float(string)
            v.append(string)

        cursor_press_past = db.cursor()
        query_press_past = """SELECT press_past
                FROM Paster_PET_2
                WHERE (date = '%(day)s')
                """ %{'day' : day}
        cursor_press_past.execute(query_press_past)
        for i in cursor_press_past.execute(query_press_past):
            string = str(i)
            string = string.replace("('", '')
            string = string.replace("',)", '')
            string = float(string)
            k.append(string)
        
    plt.clf()
    if var_flow.get() == 1:
        plt.plot(x, y , 'g')
    if var_PU.get() == 1:
        plt.plot(x, z , 'c')
    if var_temp_past.get() == 1:
        plt.plot(x, w , 'r')
    if var_temp_cool.get() == 1:
        plt.plot(x, v , 'b')
    if var_press_past.get() == 1:
        plt.plot(x, k , 'k')
    plt.show()

def valves():
    day = str(date.get())
    top = Toplevel(root)
    top.title('Valves')
    top.geometry('1220x500')
    top.resizable(0,0)
    frame = Frame(top, width="1220",height="500")
    frame.pack()
    swin = ScrolledWindow(frame, width=1220, height=500)
    swin.pack()
    win = swin.window
    canvas1 = Canvas(win, width=1220, height=16000) 
    canvas1.pack(side=LEFT, fill=BOTH, expand=True)
    Label(top, text = "                    V01        V02        V03        V04        V05        V06        V07        V08        V21        V23        V30        V31        V32        V33        V34        V35        V36        V38        V39        V40        V41        V42        V43        V44        V45        V46").place(x = 10, y=10)

    with sqlite3.connect("database.db") as db:
        
        cursor_valves = db.cursor()
        query_valves = """SELECT time, V01, V02, V03, V04, V05, V06,
                V07,V08, V21, V23, V30, V31, V32, V33, V34, V35, V36,
                V38, V39, V40, V41, V42, V43, V44, V45, V46
                FROM Valves_PET_2
                WHERE (date = '%(day)s')
                """ %{'day' : day}
        cursor_valves.execute(query_valves)
        j = 35
        for i in cursor_valves.execute(query_valves):
            Label(canvas1, text = i).place(x = 10, y = j)
            j += 20

def mnemo():
    img1 = Image.open('PET_2_mnemo_paster.jpg')
    img1.show()
    img2 = Image.open('PET_2_mnemo_buffer.jpg')
    img2.show()
    
root = Tk()
root.title('Paster PET 2')
root.geometry('180x250')
str_hour = StringVar()
var_flow = IntVar()
var_PU = IntVar()
var_temp_past = IntVar()
var_temp_cool = IntVar()
var_press_past = IntVar()

Label(text='Дата').place(x=10, y=10)
date = DateEntry(width=12, background='darkblue',foreground='white', borderwidth=2)
date.place(x=10, y=40)
Button(text="Построить график", command=plot).place(x = 10, y = 145)
Button(text="Состояния клапанов", command = valves).place(x = 10, y = 180)
Checkbutton(root, text = 'Поток',variable = var_flow, onvalue = 1, offvalue = 0).place(x = 10, y = 65)
Checkbutton(root, text = 'PU',variable = var_PU, onvalue = 1, offvalue = 0).place(x = 90, y = 65)
Checkbutton(root, text = 'Темп паст',variable = var_temp_past, onvalue = 1, offvalue = 0).place(x = 10, y = 90)
Checkbutton(root, text = 'Темп охл',variable = var_temp_cool, onvalue = 1, offvalue = 0).place(x = 90, y = 90)
Checkbutton(root, text = 'Давл паст',variable = var_press_past, onvalue = 1, offvalue = 0).place(x = 10, y = 115)
Button(text="Мнемосхема", command = mnemo).place(x = 10, y = 215)
root.mainloop()
