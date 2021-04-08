FROM python:3.7-buster

LABEL maintainer="Mike Yang <perryvm06vm06@gmail.com>"

# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY uwsgi.ini /etc/uwsgi/

ENV UWSGI_INI_FILE /app/uwsgi.ini

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Add demo app
COPY . /app

CMD ["uwsgi", "--ini", "uwsgi.ini"]
