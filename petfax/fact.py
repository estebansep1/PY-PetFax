# fact.py
from flask import (Blueprint, render_template, request, redirect)

# Define the fact blueprint
bp = Blueprint('fact', __name__, url_prefix="/facts")

# New route
@bp.route('/new')
def new():
    return render_template('facts/new.html')


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')
    
    return render_template('facts/index.html')