from tkinter import *
from tkinter import ttk
import tkinter as tk
import keyboard
import subprocess
from multiprocessing import Process


root = Tk()

# v = ttk.Scrollbar(root, orient=VERTICAL)
# h = ttk.Scrollbar(root, orient=HORIZONTAL)

# root = tk.Tk()
root.attributes('-fullscreen', True)

canvas = tk.Canvas(root, bg='white', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# h['command'] = canvas.xview
# v['command'] = canvas.yview

# ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S,E))

# canvas.grid(column=0, row=0, sticky=(N,W,E,S))
# h.grid(column=0, row=1, sticky=(W,E))
# v.grid(column=1, row=0, sticky=(N,S))
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)

# lastx, lasty = 0, 0





def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)


def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', "paletteSelected")
    canvas.itemconfigure('palette', outline='gray')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    canvas.itemconfigure("paletteSelected", outline="black")


def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
    lastx, lasty = x, y


def doneStronke(event):
    canvas.itemconfigure('currentline', width=5)


canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStronke)

id = canvas.create_rectangle((10, 10, 30, 30), fill='red', tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))

id = canvas.create_rectangle((10, 35, 30, 55), fill='black', tags=('palette', 'paletteblack'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

id = canvas.create_rectangle((10, 60, 30, 80), fill='white', tags=('palette', 'paletteeraser'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("white"))

id = canvas.create_rectangle((10, 85, 30, 105), fill='#c4f9ff', tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor('#c4f9ff'))

id = canvas.create_rectangle((30, 10, 50, 30), fill='brown', tags=('palette', 'palettebrown'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("brown"))

id = canvas.create_rectangle((10, 115, 30, 135), fill='#fff2a7', tags=('palette', 'paletteyellow'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("yellow"))

id = canvas.create_rectangle((10, 140, 30, 160), fill='#FF8ad2', tags=('palette', 'palettepink'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("pink"))

id = canvas.create_rectangle((30, 35, 50, 55), fill='#61EB57', tags=('palette', 'palettegreen'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#61EB57"))

subprocess.run(["python", "principal.py"])


def check_for_q():
    if keyboard.is_pressed('esc'):
        print("Encerrando o programa.")
        root.destroy()
    else:
        root.after(100, check_for_q)


root.after(100, check_for_q)

root.mainloop()
