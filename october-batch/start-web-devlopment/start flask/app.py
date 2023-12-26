from flask import Flask, render_template, redirect, request

myapp = Flask(__name__)


@myapp.route("/")
def myhomepage():
    return render_template("home.html")



@myapp.route("/contact/<int:abc>")
def contactus(abc):
    print(abc, "ccccccccccccccc")
    # return "this is contact s page"
    lst = [23, 10, 10, 89, 34, 23, 34, 100]
    return render_template("comtact.html",qw = abc)


@myapp.route("/login")
def loginpage():
    return render_template("authfile/login.html", name = "kriss moris")


@myapp.route("/myform")
def myform():
    return render_template("myform.html")


@myapp.route("/savethis", methods=["POST",])
def savethis():
    if request.method == "POST":
        titl = request.form.get("title")
        desc = request.form.get("msg")

        print(titl, desc)
    return redirect("/myform")


if __name__ == "__main__":
    myapp.run(debug = True)