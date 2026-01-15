from flask import Blueprint, jsonify, render_template
from flask_login import login_required, current_user

from digicheese.models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/hello')
def profile_admin():
    d = [a.to_json() for a in User.query.all()]
    return jsonify(d)

    # if current_user.has_role('admin'):
    #     return render_template('admin_profile.html', name=current_user.name)
    return render_template('profile.html', name=current_user.name)

