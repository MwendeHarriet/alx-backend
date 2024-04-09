#!/usr/bin/env python3
"""Module creates get_locale function decorator."""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Class Config."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)
babel.init_app(app)


@app.route("/")
def index():
    """Function renders 2-index.html"""
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """Function determines the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
