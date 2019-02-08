from clear.clear_function import clear_directories
from config.configuration import get_clean
import logging
from flask import Flask
from os import environ


app = Flask(__name__)
directories, files = get_clean(environ.get("APP_INI_FILE", None), app.logger)
app.logger.setLevel(logging.INFO)


@app.route('/', methods=['GET'])
def root():
    return 'file clean v0.0.1'


@app.route('/clear', methods=['DELETE'])
def clear():
    clear_directories(directories, files, app.logger)
    return 'ok'


@app.route('/reload', methods=['GET'])
def reload():
    global directories
    global files
    directories, files = get_clean(environ.get("APP_INI_FILE", None), app.logger)
    return 'ok'

