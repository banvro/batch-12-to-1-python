from flask import Flask, render_template
# from flask import render_template
myapp = Flask(__name__)

@myapp.route("/home")
def homeis():
    # return "this is a home page"
    return render_template("home.html")

@myapp.route("/about")
def aboutus():
    # return "this is about us page"
    return render_template("about.html")


if __name__ == "__main__":
    myapp.run()