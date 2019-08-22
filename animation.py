from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Drawing")
canvas.pack()

canvas.create_line(0,0, 500,400, fill="violet")
canvas.create_rectangle(100,100,200,250, fill="aqua")
canvas.create_oval(100,100,500,300, fill="hot pink")
canvas.create_polygon(500,200,50,300,180,290,111,435,152,243, fill="orchid")
canvas.create_polygon(400,10,300,300,500,300, fill="blue") 
canvas.mainloop()