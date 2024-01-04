from flask import Flask, render_template, request
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



@myapp.route("/savemydata", methods = ["POST"])
def savethis():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone_number = request.form.get("number")
        message = request.form.get("msg")

    return f"data is : {name} {email} {phone_number} {message}"


if __name__ == "__main__":
    myapp.run(debug=True)