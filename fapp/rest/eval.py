import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
#from werkzeug.security import check_password_hash, generate_password_hash

from fapp.db import get_db, query_db

bp = Blueprint('eval', __name__)

@bp.route('/rest/eval/read-table', methods=['POST'])
def read_evals():
    data = request.json
    fen = data["fen"]
    pos_id = query_db('select id from pos where fen = ?',
                [fen], one=True)
    if pos_id is None:
        return jsonify([])
    evals = query_db('select * from eval where pos_id = ?',
                [pos_id[0]])
    if pos_id is None:
        return jsonify([])
    evals = [dict(x) for x in evals]
    return jsonify(evals)
    
    
    