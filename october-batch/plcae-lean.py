import tkinter as tk

obj = tk.Tk()
obj.geometry("500x400")


lbl = tk.Label(obj, text="This is a car", font=400)
lbl.place(x = 50, y = 100)

r = tk.Checkbutton(obj, text="All Done ", font=400, bg  = "green")
r.place(x=200, y = 200) 

obj.mainloop()