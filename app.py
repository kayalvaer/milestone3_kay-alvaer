import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


#activate home page
@app.route("/")
@app.route("/home")
def home():
    #checks if user exits
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template(
            "home.html", user=user)
    else:
        return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if employee_name already registered in DB
        registered_user = mongo.db.users.find_one(
            {"employeename": request.form.get("employeename").lower()})

        if registered_user:
            flash("employeename already registered")
            return redirect(url_for("register"))
        #for unregistered user register user
        register = {
            "employeename": request.form.get("employeename").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # avail the new employee into 'session' or temporary page /cookie
        session["employee"] = request.form.get("employeename").lower()
        flash("Welcome to our Team!")
        return redirect(url_for("employee", employeename=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if employeename is registered in DB
        registered_user = mongo.db.users.find_one(
            {"employeename": request.form.get("employeename").lower()})

        if registered_user:
            # check if hashed password matches user input
            if check_password_hash(
                registered_user["password"], request.form.get("password")):
                    session["employee"] = request.form.get("employeename").lower()
                    flash("Welcome to the team, {}".format(
                        request.form.get("employeename")))
                    return redirect(url_for("employee", employeename=session["employee"]))
            else:
                # incorrect password match
                flash("Invalid Employeename and/or Password entered")
                return redirect(url_for("login"))

        else:
            # non-existing username 
            flash("Invalid Employeename and/or Password entered")
            return redirect(url_for("login"))

    return render_template("login.html")


# validate employee page
@app.route("/employee/<employeename>", methods=["GET", "POST"])
def employee(employeename):
    # get the user's employeename, url-img and title from DB
    employeename = mongo.db.users.find_one(
        {"employeename": session["employee"]})["employeename"]
    # get the session user's details from DB
    details = list(mongo.db.details.find())

    if session["employee"]:
        return render_template(
            "employee.html", employeename=employeename, details=details)

    return redirect(url_for("employee"))


# Add new employee in DB
@app.route("/add_emp", methods=["GET", "POST"])
def add_emp():
    if request.method == "POST":
        emp_info = {
            "employee_name": request.form.get("employee_name"),
            "employee_title": request.form.get("employee_title"),
            "url_img": request.form.get("url_img"),
            "password": request.form.get("password"),
            "added_by": session["user"]
        }
        mongo.db.details.insert_one(emp_info)
        return redirect("/employee/<employeename>")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
