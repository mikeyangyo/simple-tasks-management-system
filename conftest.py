from app import create_app
import pytest
from commands import run_migrations


@pytest.fixture
def app():
    app = create_app()
    app.config.from_object('configs.config.TestConfig')
    with app.app_context():
        run_migrations()
    return app
