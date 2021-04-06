from flask import Flask

from tasks.views import task_bp

app = Flask(__name__)
app.register_blueprint(task_bp)
app.url_map.strict_slashes = False
