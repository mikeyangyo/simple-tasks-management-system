FROM gitpod/workspace-full:latest

ENV PYTHONUNBUFFERED 1

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Install Poetry Dependency Management tool
USER gitpod
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH "/home/gitpod/.poetry/bin:$PATH"
RUN poetry config virtualenvs.in-project true

# git config
RUN git config --global alias.co checkout
RUN git config --global alias.ci commit
RUN git config --global alias.st status
RUN git config --global alias.br branch

# pyenv config
RUN pyenv install 3.7.10
