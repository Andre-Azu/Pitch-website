
from flask import Blueprint,render_template,request,flash
from flask_login import login_required,current_user
from .models import Pitch
from . import db

views = Blueprint('views',__name__)



@views.route('/', methods=['GET', 'POST'])
@login_required
def profile():

    if request.method == 'POST':
        pitch=request.form.get('pitch')

        if len(pitch) <=1:
            flash('Pitch too short', category='error')
        else:
            new_pitch = Pitch(data=pitch, user_id=current_user.id)
            db.session.add(new_pitch)
            db.session.commit()
            flash("Pitch added!", category="success")

    return render_template("profile.html", user=current_user)

@views.route('/product_pitch', methods=['GET', 'POST'])
@login_required
def product_pitch():
    if request.method == 'POST':
        pitch=request.form.get('pitch')

        if len(pitch) <=1:
            flash('Pitch too short', category='error')
        else:
            new_pitch = Pitch(data=pitch, user_id=current_user.id)
            db.session.add(new_pitch)
            db.session.commit()
            flash("Pitch added!", category="success")

    return render_template("product_pitch.html", user=current_user)


@views.route('/pickup_lines', methods=['GET', 'POST'])
@login_required
def pickup_lines():
    if request.method == 'POST':
        pitch=request.form.get('pitch')

        if len(pitch) <=1:
            flash('Pitch too short', category='error')
        else:
            new_pitch = Pitch(data=pitch, user_id=current_user.id)
            db.session.add(new_pitch)
            db.session.commit()
            flash("Pitch added!", category="success")

    return render_template("pickup_lines.html", user=current_user)

@views.route('/interview_pitch', methods=['GET', 'POST'])
@login_required
def interview_pitch():
    if request.method == 'POST':
        pitch=request.form.get('pitch')

        if len(pitch) <=1:
            flash('Pitch too short', category='error')
        else:
            new_pitch = Pitch(data=pitch, user_id=current_user.id)
            db.session.add(new_pitch)
            db.session.commit()
            flash("Pitch added!", category="success")

    return render_template("interview_pitch.html", user=current_user)

@views.route('/promotion_pitch', methods=['GET', 'POST'])
@login_required
def promotion():
    if request.method == 'POST':
        pitch=request.form.get('pitch')

        if len(pitch) <=1:
            flash('Pitch too short', category='error')
        else:
            new_pitch = Pitch(data=pitch, user_id=current_user.id)
            db.session.add(new_pitch)
            db.session.commit()
            flash("Pitch added!", category="success")

    return render_template("promotion.html", user=current_user)
