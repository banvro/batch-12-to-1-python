# pygame
# pyqt5

import tkinter as tk
from datetime import datetime

def myfun():
    zx = en.get()
    # new_date = datetime.strptime(zx, "%y-%m-%d")
    # print(new_date, "xxxxxxxxx")

    qw = 2023 - int(zx)
    
    lbl1.config(text = f"User age is : {qw}")


main = tk.Tk()

main.geometry("500x300")
main.title("this is my title")
main.config(background = "#17c8cf")

lbl = tk.Label(main, text = "Hwllow World", font=("robort", 30, "bold"), fg = "white", bg = "black")
lbl.pack(fill="x", padx = 20, pady = 20)


en = tk.Entry(main, font=("robort", 20, "italic"))
en.pack()

btn = tk.Button(main, text = "Submit", font =  ("xyz", 15, "bold"), command = myfun)
btn.pack(pady = 20)



lbl1 = tk.Label(main, text = "", bg = "#17c8cf")
lbl1.pack()

main.mainloop()


# 1) pack()
# 2) grid()
# 3) place