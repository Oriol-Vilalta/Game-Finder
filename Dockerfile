FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /gameFinder
COPY Pipfile Pipfile.lock /gameFinder/
RUN pip install pipenv && pipenv install --system
COPY . /gameFinder/
