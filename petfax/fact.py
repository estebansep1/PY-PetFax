# fact.py
from flask import (Blueprint, render_template, request, redirect)
from . import models

# Define the fact blueprint
bp = Blueprint('fact', __name__, url_prefix="/facts")

# New route
@bp.route('/new')
def new():
    return render_template('facts/new.html')


@bp.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = models.Fact(submitter=submitter,fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')

    results = models.Fact.query.all()
    for result in results:
        print(result)

    return render_template('facts/index.html', facts=results)