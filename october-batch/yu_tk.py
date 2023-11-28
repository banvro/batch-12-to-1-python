# pygame
# pyqt5

import tkinter as tk

main = tk.Tk()

main.geometry("500x300")
main.title("this is my title")
main.config(background = "#17c8cf")

lbl = tk.Label(main, text = "Hwllow World", font=("robort", 30, "bold"), fg = "white", bg = "black")
lbl.pack(fill="x", padx = 20, pady = 20)


en = tk.Entry(main, font=("robort", 20, "italic"))
en.pack()




main.mainloop()


# 1) pack()
# 2) grid()
# 3) place