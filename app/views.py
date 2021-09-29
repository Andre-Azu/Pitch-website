from flask import Blueprint,render_template


views = Blueprint('views',__name__)

@views.route('/')
def profile():
    return render_template("profile.html")
