import tkinter as tk
import joblib
import numpy as np

mymodel = joblib.load("insurence-predictor.joblib")

def insurncepredict():
    userage = ent.get()

    userinputage = np.array(int(userage))
    reshapeage = userinputage.reshape(-1, 1)

    xyz = mymodel.predict(reshapeage)

    if xyz[0] == 0:
        lblshow.config(text = "User is not getting to buy insurence")
    
    else:
        lblshow.config(text = "User buy the insurence")


app = tk.Tk()
app.geometry("500x300")
app.title("Insurence Predictor")
app.config(background = "light green")


lbl = tk.Label(app, text = "Enter Age", font = ("robort", 30, "bold"), bg = "light green")
lbl.pack(pady=20)

ent = tk.Entry(app, font = ("robort", 23, "bold"))
ent.pack()

btn = tk.Button(app, text = "Check", font = ("robort", 18, "bold"), command = insurncepredict) 
btn.pack(ipadx=30, pady=20)

lblshow = tk.Label(app, text = "", font = ("robort", 18, "italic"), bg = "light green")
lblshow.pack()

app.mainloop()