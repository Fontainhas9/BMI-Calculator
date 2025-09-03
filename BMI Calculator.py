from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.configure(bg="#f0f1f5")
root.resizable(False, False)

# --- Caminho seguro para as imagens ---
base_dir = os.path.dirname(os.path.abspath(__file__))


def load_image(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Imagem não encontrada: {path}")
    return path

# --- Função para calcular BMI ---


def BMI():
    try:
        h = float(Height.get())
        w = float(Weight.get())
    except ValueError:
        label1.config(text="")
        label2.config(text="Erro")
        label3.config(text="Digite números válidos para altura e peso.")
        return

    if h <= 0 or w <= 0:
        label1.config(text="")
        label2.config(text="Erro")
        label3.config(text="Altura e peso devem ser positivos.")
        return

    bmi = round(float(w / h**2), 1)
    label1.config(text=bmi)

    if bmi <= 18.5:
        label2.config(text="Underweight", fg="blue")
        label3.config(
            text="Você está abaixo do peso.\nConsidere consultar um médico.", fg="blue")
    elif 18.5 < bmi <= 24.9:
        label2.config(text="Normal", fg="green")
        label3.config(
            text="Você está com peso normal.\nMantenha assim!", fg="green")
    elif 25 <= bmi <= 29.9:
        label2.config(text="Overweight", fg="orange")
        label3.config(
            text="Você está acima do peso.\nConsidere consultar um médico.", fg="orange")
    elif 30 <= bmi <= 34.9:
        label2.config(text="Obese", fg="red")
        label3.config(
            text="Você está obeso.\nConsidere consultar um médico.", fg="red")
    else:
        label2.config(text="Obese ++", fg="darkred")
        label3.config(
            text="Você está extremamente obeso.\nConsulte um médico.", fg="darkred")


# --- Carregar imagens ---
image_icon = PhotoImage(file=load_image("icon.png"))
root.iconphoto(False, image_icon)

top_image_file = load_image("top.png")
top_image = PhotoImage(file=top_image_file)
Label(root, image=top_image, bg="#f0f1f5").place(x=-10, y=-10)

box_file = load_image("box.png")
box_img = PhotoImage(file=box_file)
Label(root, image=box_img).place(x=20, y=100)
Label(root, image=box_img).place(x=240, y=100)

secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y=430)

# --- Entradas de altura e peso ---
Height = StringVar()
Weight = StringVar()

height_entry = Entry(root, textvariable=Height, width=10, font="arial 30",
                     fg="#000", bd=0, bg="#fff", justify=CENTER)
height_entry.place(x=35, y=160)
height_entry.insert(0, "1.70")

weight_entry = Entry(root, textvariable=Weight, width=10, font="arial 30",
                     fg="#000", bd=0, bg="#fff", justify=CENTER)
weight_entry.place(x=255, y=160)
weight_entry.insert(0, "70")

# --- Botão para calcular BMI ---
calculate_btn = Button(
    root,
    text="Calcular BMI",
    width=20,
    height=2,
    font="arial 12 bold",
    bg="#1f6e68",
    fg="white",
    command=BMI
)
calculate_btn.place(x=140, y=250)

# --- Labels de resultado (reposicionados acima do rodapé) ---
label1 = Label(root, font="arial 50 bold", fg="#000", bg="#f0f1f5")
label1.place(x=180, y=320)

label2 = Label(root, font="arial 20 bold", fg="#3b3a3a", bg="#f0f1f5")
label2.place(x=150, y=400)

label3 = Label(root, font="arial 12", bg="#f0f1f5")
label3.place(x=80, y=430)

# --- Rodapé ---
Label(root, width=470, height=80, bg="lightblue").place(x=0, y=500)

root.mainloop()
