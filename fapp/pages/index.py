import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash

from fapp.db import get_db

bp = Blueprint('index', __name__, static_folder='static')

@bp.route('/')
def root():
    return bp.send_static_file('index.html')