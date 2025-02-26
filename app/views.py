from app import app
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime

def format_date_joined(date):
    return date.strftime("%B, %Y")  # "January, 2018"

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Paul Bailey")

@app.route('/profile')
def profile():
    """Render the website's profile page."""
    user = {
        "full_name": "Paul Bailey",
        "username": "pbailey29",
        "location": "Kingston, Jamaica",
        "date_joined": format_date_joined(datetime(2018, 1, 10)),
        "bio": "I am a smart and talented young man who loves website design and development. Contact me if you'd like to work together on a new project.",
        "posts": 7,
        "following": 100,
        "followers": 250,
        "profile_pic": "profile.jpg"
    }
    return render_template('profile.html', user=user)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
