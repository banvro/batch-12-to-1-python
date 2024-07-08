# Tkinter --> python gui

import tkinter as tk
import joblib #pip install joblib
import numpy as np #pip install numpy

model = joblib.load("packge-predictor.joblib")

def mypredctor():
    cgpa = ent.get()
    cgpa = np.array([float(cgpa)])
    new_cgpa = cgpa.reshape(-1, 1)
    # print(new_cgpa.shape, "xxxxxxxxxx")
    pkg = model.predict(new_cgpa)
    pkg = str(pkg[0])
    newpkg = pkg[ : 4]

    showpkg.config(text = f"Your Package is : {newpkg}")

    ent.delete(0, tk.END)

app = tk.Tk()
app.geometry("600x300")
app.title("Package Predictor")
app.config(background = "#8fed5c")

header = tk.Label(app, text = "Check Your Package on CGPA", font = ("robort", 20, "bold"), background = "yellow")
header.pack(fill = "x", ipady = 10)

lbl = tk.Label(app, text = "Enter CGPA", font = ("robort",  30, "bold"), foreground = "#2f730a", background = "#8fed5c")
lbl.pack(pady = 17)


ent = tk.Entry(app, font = ("robort", 20, "italic"))
ent.pack()

btn = tk.Button(app, text = "Check pkg", font = ("robort", 15, "bold"), bg = "green", fg = "lightgreen", command = mypredctor)
btn.pack(pady = 17)

showpkg = tk.Label(app, text = "", foreground = "#2f730a", background = "#8fed5c", font = ("robort", 15))
showpkg.pack()



app.mainloop()