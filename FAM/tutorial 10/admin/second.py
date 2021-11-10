from flask import Blueprint, render_template

second1 = Blueprint("second", __name__, static_folder="/admin/static", template_folder= "/admin/templates")

@second1.route("/home")
@second1.route("/")
def home():
    print(second1.template_folder)
    return render_template("home.html")