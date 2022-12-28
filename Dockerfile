FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY . /code

RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m pip install Pillow
RUN pip install django-crispy-forms
