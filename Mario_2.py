from PIL import Image, ImageTk
import tkinter as tk

# Crea una ventana
root = tk.Tk()
root.geometry("1000x1000")

# Carga la imagen y crea un objeto ImageTk
image = Image.open('mario2.png')
photo = ImageTk.PhotoImage(image)

# Crea un widget Canvas y muestra la imagen
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack()
canvas.create_image(0, 0, image=photo, anchor=tk.NW)

# Animación
x = 0
y = 0
dx = 5
dy = 5

def animate():
    global x, y, dx, dy
    canvas.move(tk.ALL, dx, dy)
    x += dx
    y += dy
    if x < 0 or x > canvas.winfo_width() - image.width:
        dx *= -1
    if y < 0 or y > canvas.winfo_height() - image.height:
        dy *= -1
    root.after(50, animate)

# Inicia la animación
animate()

# Ejecuta el loop principal de la ventana
root.mainloop()
