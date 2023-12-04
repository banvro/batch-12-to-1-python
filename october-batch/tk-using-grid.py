# # grid 


# import tkinter as tk

# window = tk.Tk()
# window.geometry("500x300")
# window.title("this is my title")
# window.config(background="yellow")

# # lbl = tk.Label(window, text = "Hwlloo World", font = ("Rbert", 20, "bold"))
# # # lbl.pack(side = "top")

# # ent = tk.Entry(window)
# # # ent.pack()



# window.mainloop()





# # 1) pack()
# # 2) grid()
# # 3) place()






import tkinter as tk
import mysql.connector

# con = mysql.connector.connect(host="localhost", username = "root", pssword = "1234", database = "yourdatabasename")
# cursr = con.cursor()

# cursr.execute("show database Like %s", ("Studnets",))
# zx = cursr.fetchone()

# if not zx:
#     cursr.execute("Create database Students")

def savedata():
    name = ent1.get()
    age = ent2.get()
    emial = ent3.get()
    numbr = ent4.get()

    # cursr.execute(f"insert ito tblname values('{name}', {age},' {emial}', '{numbr}')")
    # con.commit()

    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)
    ent3.delete(0, tk.END)
    ent4.delete(0, tk.END)

    mymsg.config(text = "data saved sv=ucsessfullyy" )
    


window = tk.Tk()
window.geometry("600x400")
window.title("this is my title")
window.config(background="yellow")


lbl1 = tk.Label(window, text = "", font = ("bobort", 20, "bold"), bg = "yellow")
lbl2 = tk.Label(window, text = "Name", font = ("bobort", 20, "bold"), bg = "yellow")
lbl3 = tk.Label(window, text = "Age", font = ("bobort", 20, "bold"), bg = "yellow")
lbl4 = tk.Label(window, text = "Email", font = ("bobort", 20, "bold"), bg = "yellow")
lbl5 = tk.Label(window, text = "Number", font = ("bobort", 20, "bold"), bg = "yellow")

lbl6 = tk.Label(window, text = ":", font = ("bobort", 20, "bold"), bg = "yellow")
lbl7 = tk.Label(window, text = ":", font = ("bobort", 20, "bold"), bg = "yellow")
lbl8 = tk.Label(window, text = ":", font = ("bobort", 20, "bold"), bg = "yellow")
lbl9 = tk.Label(window, text = ":", font = ("bobort", 20, "bold"), bg = "yellow")

mymsg = tk.Label(window, text = "  ", font = ("bobort", 20, "bold"), bg = "yellow", fg="Green")

ent1 = tk.Entry(window, font = ("robort", 20, "italic"))
ent2 = tk.Entry(window, font = ("robort", 20, "italic"))
ent3 = tk.Entry(window, font = ("robort", 20, "italic"))
ent4 = tk.Entry(window, font = ("robort", 20, "italic"))

btn = tk.Button(window, text="Submit", font = ("robort", 20, "bold"), command = savedata)


lbl1.grid(row=0, column=0, padx=25)
lbl2.grid(row=1, column=1, pady=8)
lbl3.grid(row=2, column=1, pady=8)
lbl4.grid(row=3, column=1, pady=8)
lbl5.grid(row=4, column=1, pady=8)

lbl6.grid(row=1, column=2)
lbl7.grid(row=2, column=2)
lbl8.grid(row=3, column=2)
lbl9.grid(row=4, column=2)

ent1.grid(row=1, column=3, padx=5)
ent2.grid(row=2, column=3)
ent3.grid(row=3, column=3)
ent4.grid(row=4, column=3)

btn.grid(row=5, column=3)

mymsg.grid(row=6, column=3)

window.mainloop()