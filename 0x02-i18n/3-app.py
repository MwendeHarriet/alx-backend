#!/usr/bin/env python3
"""Module to parametrize templates."""

from flask import Flask, request, render_template
from flask_babel import Babel


class Config():
    """Class Config."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Function determines the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """Function renders 3-index.html."""
    return render_template("3-index.html")


# babel.init_app(app, locale_selector=get_locale)
# Use the above instead of @babel.localeselector to avoid error


if __name__ == "__main__":
    app.run()
