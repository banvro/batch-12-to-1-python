from flask import Flask, render_template, request, redirect
import mysql.connector
import os

conn = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "amazon")

cuser = conn.cursor()

myapp=Flask(__name__)
@myapp.route("/")
def homeis():
    # return "this is a homepage"
    return render_template("newhome.html")

@myapp.route("/about")
def aboutus():
    # return "this is about us page"
    return render_template("about.html")

@myapp.route("/save-this-data",methods=["POST"])
def savethis():
    if request.method == "POST":
        name = request.form.get("name")
        thisemail = request.form.get("email")
        phnumber = request.form.get("number")
        msg = request.form.get("msg")
        img = request.files.get("imgx")
        # img = request.files["imgx"]

        if img:
            img.save(os.path.join("static/myimages/", img.filename))
            image_path = os.path.join("static/myimages/", img.filename)


        cuser.execute(f"insert into savemydataa values('{name}', '{phnumber}', '{thisemail}', '{msg}', '{image_path}')")
        conn.commit()
        return redirect("/showdata")

    return f"Data Saved !"

@myapp.route("/showdata")
def showingthis():
    dt = request.args.get("query")
    if dt:
        cuser.execute(f"select * from savemydataa where Name = '{dt}'")
        alldata = cuser.fetchall()
    else:
        cuser.execute("select * from savemydataa;")
        alldata = cuser.fetchall()
    # print(alldata, "all data")
    return render_template("showthisdata.html", allrecords = alldata)

@myapp.route("/deletethis/<xyz>", methods = ["POST"])
def deletdata(xyz):
    cuser.execute(f"delete from savemydataa where Name = '{xyz}'")
    conn.commit()
    return redirect("/showdata")

@myapp.route("/updatedata/<abc>", methods = ["POST"])
def updateshow(abc):
    cuser.execute(f"select * from savemydataa where Name = '{abc}'")
    rec = cuser.fetchone()

    return render_template("updatethisfome.html", data = rec)


@myapp.route("/updatehow/<x>", methods = ["POST"])
def updtehownow(x):
    if request.method == "POST":
        name = request.form.get("name")
        thisemail = request.form.get("email")
        phnumber = request.form.get("number")
        msg = request.form.get("msg")
        cuser.execute(f"update savemydataa set Name = '{name}', email = '{thisemail}', Number =' {phnumber}', message = '{msg}' where Name = '{x}'")
        conn.commit()
    return redirect("/showdata")



if __name__ =="__main__":
    myapp.run(debug = True)