from flask import render_template, request, redirect, flash
from app import app

workouts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_workout():
    workout = request.form['workout']
    duration = request.form['duration']

    if not workout or not duration:
        flash("Please enter both workout and duration.")
        return redirect('/')

    try:
        duration = int(duration)
        workouts.append({'workout': workout, 'duration': duration})
        flash(f"'{workout}' added successfully!")
    except ValueError:
        flash("Duration must be a number.")
    return redirect('/')

@app.route('/view')
def view_workouts():
    return render_template('workouts.html', workouts=workouts)