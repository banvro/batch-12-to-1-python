import tkinter as tk
import joblib

mymodel = joblib.load("Student_Performance_model_checker.joblib")


def checkfrerence():
    x = ent1.get()
    y = ent2.get()

    cofii = mymodel.coef_
    intercept = mymodel.intercept_

    # print(cofii)
    # print(intercept)

    prefrence = intercept + cofii[0]*float(x) + cofii[1] * float(y)

    lblshow.config(text = f"Your Performance Index is : {str(prefrence)[:5]}")

app = tk.Tk()
app.geometry("500x400")
app.title("Performence checker")

f1 = tk.Frame(app, relief = "ridge", borderwidth = 20, bg = "light green")
f1.pack(fill="x")

f2 = tk.Frame(app, relief = "sunken", borderwidth = 20, bg = "light yellow")
f2.pack(fill="x")


lbl = tk.Label(f1, text = "Student Performance", font = ("robort", 20, "bold"), bg = "light green")
lbl.pack(pady=12)

lbl2 = tk.Label(f2,  text = "", font = ("robort", 20, "bold"), bg = "light yellow")
lbl3 = tk.Label(f2,  text = "Hours Studied", font = ("robort", 15, "bold"), bg = "light yellow")
lbl4 = tk.Label(f2,  text = "Previous Scores", font = ("robort", 15, "bold"), bg = "light yellow")

lbl5 = tk.Label(f2,  text = ":", font = ("robort", 15, "bold"), bg = "light yellow")
lbl6 = tk.Label(f2,  text = ":", font = ("robort", 15, "bold"), bg = "light yellow")

ent1 = tk.Entry(f2, font = ("robort", 15, "italic"))
ent2 = tk.Entry(f2, font = ("robort", 15, "italic"))

lbl2.grid(row=0, column=0)
lbl3.grid(row=1, column=1)
lbl4.grid(row=2, column=1)

lbl5.grid(row=1, column=2, padx=10)
lbl6.grid(row=2, column=2)

ent1.grid(row=1, column=3)
ent2.grid(row=2, column=3, pady=10)

btn = tk.Button(f2, text = "Check", font=("robort", 15, "bold"), bg = "green", fg = "white", command = checkfrerence)
btn.grid(row=3, column=3)


f3 = tk.Frame(app, relief="groove", borderwidth=15, bg = "light pink")
f3.pack(fill="x")

lblshow = tk.Label(f3,  text = "",  font = ("robort", 18), fg = "green",  bg = "light pink")
lblshow.pack()

app.mainloop()