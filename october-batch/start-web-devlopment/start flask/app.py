from flask import Flask

myapp = Flask(__name__)


@myapp.route("/rdd")
def myhomepage():
    return "this is a home page"



@myapp.route("/contact")
def contactus():
    return "this is contact s page"



if __name__ == "__main__":
    myapp.run(debug = True)