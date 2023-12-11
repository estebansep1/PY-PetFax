# pet.py
from flask import Blueprint, render_template
import json

# Load pets data
pets = json.load(open('pets.json'))

# Define the pet blueprint
pet_bp = Blueprint('pet', __name__, url_prefix="/pets")

# Index route
@pet_bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

# Show route
@pet_bp.route('/<int:index>')
def show(index):
    pet = pets[index]
    return render_template('pets/show.html', pet=pet)
