import tkinter as tk
import joblib
import numpy as np

model = joblib.load("Student_performance_predictor.joblib")

def predciter():
    x1 = ent1.get()
    x2 = ent2.get()
    x3 = ent3.get()
    x4 = ent4.get()

    beats = model.coef_
    intercept = model.intercept_
    
    # y = b0 + b1x1 + b2x2 + b3x3 + b4x4

    y = intercept + beats[0]*float(x1) + beats[1]*float(x2) + beats[2]*float(x3) + beats[3]*float(x4)

    lblhow.config(text = f"Performence Score : {y}")

app = tk.Tk()
app.geometry("650x560")
app.title("Stduent Performence Predictor")
app.config(background = "lightblue")

frame1 = tk.Frame(app, relief = "raised", borderwidth = 14)
frame1.pack(fill = "x")

label = tk.Label(frame1, text = "Performence Predictor", font = ("robort", 21, "bold"))
label.pack(pady = 9)


frame2 = tk.Frame(app, relief = "groove", borderwidth = 14)
frame2.pack(fill = "x")

lbl1 = tk.Label(frame2, text = "")
lbl1.grid(row = 0, column = 0, padx = 14, pady = 8)

lbl1 = tk.Label(frame2, text = "Hours Studied", font = ("robort", 20, "bold"))
lbl2 = tk.Label(frame2, text = "Previous Scores", font = ("robort", 20, "bold"))
lbl3 = tk.Label(frame2, text = "Sleep Hours", font = ("robort", 20, "bold"))
lbl4 = tk.Label(frame2, text = "Sample Papers", font = ("robort", 20, "bold"))

lbl5 = tk.Label(frame2, text = ":", font = ("robort", 20, "bold"))
lbl6 = tk.Label(frame2, text = ":", font = ("robort", 20, "bold"))
lbl7 = tk.Label(frame2, text = ":", font = ("robort", 20, "bold"))
lbl8 = tk.Label(frame2, text = ":", font = ("robort", 20, "bold"))

ent1 = tk.Entry(frame2, font = ("robort", 20, "bold"))
ent2 = tk.Entry(frame2, font = ("robort", 20, "bold"))
ent3 = tk.Entry(frame2, font = ("robort", 20, "bold"))
ent4 = tk.Entry(frame2, font = ("robort", 20, "bold"))

lbl1.grid(row = 1, column = 1, pady = 6)
lbl2.grid(row = 2, column = 1, pady = 6)
lbl3.grid(row = 3, column = 1, pady = 6)
lbl4.grid(row = 4, column = 1, pady = 6)

lbl5.grid(row = 1, column = 2, padx = 5)
lbl6.grid(row = 2, column = 2, padx = 5)
lbl7.grid(row = 3, column = 2, padx = 5)
lbl8.grid(row = 4, column = 2, padx = 5)

ent1.grid(row = 1, column = 3)
ent2.grid(row = 2, column = 3)
ent3.grid(row = 3, column = 3)
ent4.grid(row = 4, column = 3)

frame3 = tk.Frame(app, relief = "sunken", borderwidth = 17)
frame3.pack(fill = "x")

btn = tk.Button(frame3, text = "Predict", font = ("robort", 18, "bold"), command = predciter)
btn.pack()

frame4 = tk.Frame(app, relief = "sunken", borderwidth = 17)
frame4.pack(fill = "x", pady=10)

lblhow = tk.Label(frame4, text = "", font = ("robort", 20, "bold"))
lblhow.pack()

app.mainloop()