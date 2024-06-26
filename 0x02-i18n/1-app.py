#!/usr/bin/env python3
"""Module is a basic babel setup."""

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
    """Function renders 1-index.html."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
