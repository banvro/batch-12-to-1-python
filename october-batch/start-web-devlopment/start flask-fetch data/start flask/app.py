from flask import Flask, render_template, request, redirect
import mysql.connector

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

        cuser.execute(f"insert into savemydataa values('{name}', '{phnumber}', '{thisemail}', '{msg}')")
        conn.commit()
        return redirect("/showdata")

    return f"Data Saved !"

@myapp.route("/showdata")
def showingthis():
    cuser.execute("select * from savemydataa;")
    alldata = cuser.fetchall()
    # print(alldata, "all data")
    return render_template("showthisdata.html", allrecords = alldata)


if __name__ =="__main__":
    myapp.run(debug = True)