import tkinter as tk
#  pip install joblib
import joblib

model = joblib.load("user-package-recoginzer-slr.joblib")

def checkypkg():
    cgpa = ent.get()

    m = model.coef_
    b = model.intercept_

    y = m[0] * float(cgpa) + b

    lblx.config(text = f"Your CGPA is : {y}")



app = tk.Tk()
app.geometry("500x300")

lbl = tk.Label(app, text= "Enter Your CGPA", font = ("robort", 20, "bold"))
lbl.pack(pady = 15)

ent = tk.Entry(app, font = ("robort", 25, "italic"))
ent.pack()

btn = tk.Button(app, text="Check CGPA", font = ("robort", 20, "bold"), bg = "yellow", command = checkypkg)
btn.pack(pady=15)


lblx = tk.Label(app, text = "", fg = "green", font = ("robort", 15))

lblx.pack()

app.mainloop()