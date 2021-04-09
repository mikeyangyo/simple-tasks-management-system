from app import create_app
import pytest


@pytest.fixture
def app():
    app = create_app()
    app.config.from_object('configs.config.TestConfig')
    return app
