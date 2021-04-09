from flask import Flask, jsonify

from tasks.views import task_bp
from utils.enums import HttpStatusCode


def create_app():
    app = Flask(__name__)

    # config app
    app.config.from_object('configs.config.Config')

    # register blueprints
    app.register_blueprint(task_bp)

    # configurations
    app.url_map.strict_slashes = False

    # error handlers
    @app.errorhandler(HttpStatusCode.InternalError.value)
    def occur_internal_error(e):
        error_msg = str(e) or 'Internal Error'
        return jsonify(error=error_msg), HttpStatusCode.InternalError.value

    @app.errorhandler(HttpStatusCode.NotFound.value)
    def resource_not_found(e):
        error_msg = str(e) or 'Resource Not Found'
        return jsonify(error=error_msg), HttpStatusCode.NotFound.value

    @app.errorhandler(HttpStatusCode.BadRequest.value)
    def bad_request(e):
        error_msg = str(e) or 'Bad Request'
        return jsonify(error=error_msg), HttpStatusCode.BadRequest.value

    return app


app = create_app()
