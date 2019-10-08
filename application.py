from flask import Flask, render_template, request, redirect

app = Flask(__name__)

fellows = []

@app.route("/")         # / is homepage rendering
def index():
    name = request.args.get("name", "Aliyu")
    return render_template("index.html", name=name)

@app.route("/registerants")
def registeredfellows():
    return render_template("registered.html", fellows=fellows)

@app.route("/register", methods=["GET"])
def registerform():
    return render_template("register.html")


@app.route("/register", methods=["POST"])         # register page rendering
def register():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    email = request.form.get("email")
    Location = request.form.get("Location")

    if not firstname or not email:
        return render_template("failure.html")
    fellows.append(f"{firstname} from {Location} state of Nigeria")
    return redirect("/registerants")

# @app.route("/AboutUs")
# def about_us():
#     name = request.args.get("name")
#     return render_template("aboutUs")

# @app.route("/ContactUs")         # / is contact us rendering
# def Contact_us():
#     name = request.args.get("name")
#     return render_template("contactUs.html", name=name)
    