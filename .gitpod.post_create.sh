# install dependencies
export PIP_USER=false
poetry install
poetry run pre-commit install --install-hooks
