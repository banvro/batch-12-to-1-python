from flask import Flask, render_template

myapp = Flask(__name__)


@myapp.route("/")
def myhomepage():
    return render_template("home.html")



@myapp.route("/contact")
def contactus():
    # return "this is contact s page"
    return render_template("comtact.html")


@myapp.route("/login")
def loginpage():
    return render_template("authfile/login.html")


if __name__ == "__main__":
    myapp.run(debug = True)