# fact.py
from flask import Blueprint, render_template

# Define the fact blueprint
fact_bp = Blueprint('fact', __name__, url_prefix="/facts")

# New route
@fact_bp.route('/new')
def new():
    return render_template('facts/new.html')
