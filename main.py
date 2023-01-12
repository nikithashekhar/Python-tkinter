from tkinter import *
from tkinter import ttk
import random
from quick import quick_sort
 
root = Tk()
root.title("Quick Sort Visualizer")

root.maxsize(900, 600)
root.config(bg="Black")
 
select_alg = StringVar()
data = []
 
def generate():
 
    global data
 
    minval = int(minEntry.get())
 
    maxval = int(maxEntry.get())

    sizeval = int(sizeEntry.get())
 
    data = []
    for _ in range(sizeval):
        data.append(random.randrange(minval, maxval+1))
 
    drawData(data, ['Red' for x in range(len(data))])

    print("Data generated")

def drawData(data, colorlist):
    canvas.delete("all")
    can_height = 380
    can_width = 550
    x_width = can_width/(len(data) + 1)
    offset = 30
    spacing = 10
 
    normalized_data = [i / max(data) for i in data]
 
    for i, height in enumerate(normalized_data):

        x0 = i*x_width + offset + spacing
        y0 = can_height - height*340
 
        x1 = ((i+1)*x_width) + offset
        y1 = can_height
 
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
        canvas.create_text(x0+2, y0, anchor=SE, text=str(data[i]))
    root.update_idletasks()

def start_algorithm():
    global data
 
    if not data:
        return
 
    if (algmenu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data)-1, drawData, speedbar.get())
        drawData(data, ['Green' for x in range(len(data))])

    print("Sorting started")

def quickSort_code():

    code = Tk()
    code.title("Quick Sort Code")
    code.maxsize(900, 600)
    code.config(bg="Black")

    Quick = Canvas(code, width=600, height=380, bg="White")
    Quick.grid(row=1, column=0, padx=10, pady=5)
    Quick.create_text(300, 150, text=(open("quickSort.txt")).read(), fill="black", font=('Helvetica'))
    Quick.pack()

    print("Code displayed")

Mainframe = Frame(root, width=600, height=200, bg="Grey")
Mainframe.grid(row=0, column=0, padx=10, pady=5)
 
canvas = Canvas(root, width=600, height=380, bg="White")
canvas.grid(row=1, column=0, padx=10, pady=5)

about = Frame(root, width=600, height=100, bg="White")
about.grid(row=2, column=0, padx=10, pady=5)
 
Label(Mainframe, text="ALGORITHM", bg='Grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
Label(about, text="Nikitha Shekhar (20GACSE046)", bg='white').grid(row=2, column=0, padx=5, pady=5, sticky=W)

algmenu = ttk.Combobox(Mainframe, textvariable=select_alg,  values=["Quick Sort"])
algmenu.grid(row=0, column=1, padx=5, pady=5)
algmenu.current(0)
 
Button(Mainframe, text="Start", bg="Blue", command=start_algorithm).grid(row=1, column=3, padx=5, pady=5)
 
speedbar = Scale(Mainframe, from_=0.10, to=2.0, length=100, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed")
speedbar.grid(row=0, column=2, padx=5, pady=5)

sizeEntry = Scale(Mainframe, from_=3, to=60, resolution=1, orient=HORIZONTAL, label="Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(Mainframe, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Minimum Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(Mainframe, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Maximum Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(Mainframe, text="Generate", bg="Red", command=generate).grid(row=0, column=3, padx=5, pady=5)

Button(about, text="Get Code", bg="Green", command=quickSort_code).grid(row=2, column=1, padx=5, pady=5)
root.mainloop()