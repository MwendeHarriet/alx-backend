#!/usr/bin/env python3
"""Module mock logging in."""

from flask import Flask, request, render_template, g
from flask_babel import Babel


class Config:
    """Class Config."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """Functions returns a user dictionary or None if the ID cannot be found or
    if login_as was not passed."""
    user_id = request.args.get('login_as')
    if user_id is not None and int(user_id) in users.keys():
        return users.get((int(user_id)))
    return None


@app.before_request
def before_request():
    """Functions uses get_user to find a user if any, and set it as a
    global on flask.g.user."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Function determines the best match with our supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """Functions renders 5-index.html."""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
