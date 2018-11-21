from flask import render_template, request, flash, redirect, url_for

from app.auth.forms import RegistrationForm

from app.auth import authentication as at


@at.route('/registration')
def register_user():
    form = RegistrationForm()  # book data is fetch from db table here and queries store in books
    return render_template('registration.html', form=form)  # using render template method sending the books variable to



