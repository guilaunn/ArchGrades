FROM python:3.9.6
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt \
    && pip install --upgrade pip
Copy . /usr/src/app \
