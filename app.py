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


#activate epics and stories
@app.route("/")
@app.route("/get_epics")
def get_epics():
    epics = list(mongo.db.epics.find())
    return render_template("epics.html", epics=epics)


#activate home page
@app.route("/")
@app.route("/home")
def home():
    #checks if employee exits
    if "user" in session:
        user = mongo.db.users.find_one(
            {"employeename": session["user"]})["employeename"]
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
        return redirect(url_for("employee", employeename=session["employee"]))
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

    return redirect(url_for("login"))


# Add more employee details in DB
@app.route("/add_info", methods=["GET", "POST"])
def add_info():
    if request.method == "POST":
        info = {
            "info_name": request.form.get("info_name"),
            "url_img": request.form.get("url_img"),
            "emp_title": request.form.get("emp_title"),
            "password": request.form.get("password"),
            
        }
        mongo.db.details.insert_one(info)
        return redirect("/employee/<employeename>")


# Add page to see employee
@app.route("/view_info/<info_name>")
def view_info(info_name):
    info = mongo.db.details.find_one({"_id": ObjectId(info_name)})
    return render_template("view_info.html", info=info)


@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You are now signed out!")
    session.pop("employee")
    return redirect(url_for("login"))


@app.route("/add_epic", methods=["GET", "POST"])
def add_epic():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        epic = {
            "product_name": request.form.get("product_name"),
            "epic_name": request.form.get("epic_name"),
            "story_description": request.form.get("story_description"),
            "product_owner": request.form.get("product_owner"),
            "lead_developer": request.form.get("lead_developer"),
            "due_date": request.form.get("due_date"),
            "is_urgent": is_urgent,
            
        }
        mongo.db.epics.insert_one(epic)
        flash("New epic now added")
        return redirect(url_for("get_epics"))

    products = mongo.db.products.find().sort("product_name",1)
    return render_template("add_epic.html", products=products)


@app.route("/edit_epic/<epic_id>", methods=["GET", "POST"])
def edit_epic(epic_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "product_name": request.form.get("product_name"),
            "epic_name": request.form.get("epic_name"),
            "story_description": request.form.get("story_description"),
            "product_owner": request.form.get("product_owner"),
            "lead_developer": request.form.get("lead_developer"),
            "due_date": request.form.get("due_date"),
            "is_urgent": is_urgent,
        }
        mongo.db.epics.update({"_id": ObjectId(epic_id)}, submit)
        flash("Successfully Updated Changes")

    epic = mongo.db.epics.find_one({"_id": ObjectId(epic_id)})
    products = mongo.db.products.find().sort("product_name", 1)
    return render_template("edit_epic.html", epic=epic, products=products)


@app.route("/delete_epic/<epic_id>")
def delete_epic(epic_id):
    mongo.db.epics.remove({"_id": ObjectId(epic_id)})
    flash("Deleted the epic now!")
    return redirect(url_for("get_epics"))


# 404 page not found error
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error=error), 404


# 500 internal server error
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
