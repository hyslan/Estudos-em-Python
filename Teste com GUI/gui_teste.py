import tkinter as tk
import random

def mover_bola():
    canvas.move(bola, velocidade_x, velocidade_y)
    pos = canvas.coords(bola)
    if pos[2] >= 400 or pos[0] <= 0:
        velocidade_x = -velocidade_x
    if pos[3] >= 400 or pos[1] <= 0:
        velocidade_y = -velocidade_y
    root.after(50, mover_bola)

def mover_barra(event):
    canvas.move(barra, event.x - pos_x, 0)
    pos_x = event.x

root = tk.Tk()
root.geometry("400x400")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

bola = canvas.create_oval(0, 0, 20, 20, fill="red")
barra = canvas.create_rectangle(175, 380, 225, 400, fill="blue")

velocidade_x = 5
velocidade_y = 5
pos_x = 200

canvas.bind("<Motion>", mover_barra)
mover_bola()
root.mainloop()
