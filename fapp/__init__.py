import os

from flask import Flask, send_from_directory


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'maindb.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/js/<path:path>')
    def send_js(path):
        return send_from_directory('js', path)
    @app.route('/css/<path:path>')
    def send_css(path):
        return send_from_directory('css', path)

    @app.route('/img/<path:path>')
    def send_img(path):
        return send_from_directory('img', path)

    from .pages import index
    app.register_blueprint(index.bp)

    from .rest import eval
    app.register_blueprint(eval.bp)

    from . import db
    db.init_app(app)

    return app