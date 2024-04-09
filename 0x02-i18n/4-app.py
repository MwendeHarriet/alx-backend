#!/usr/bin/env python3
"""Module  implement a way to force a particular locale by passing the
    locale=fr parameter to your app’s URLs."""

from flask import Flask, request, render_template
from flask_babel import Babel


class Config(object):
    """Class Config."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index() -> str:
    """Function renders 4-index.html."""
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
    """Function determines the best match with our supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run()
