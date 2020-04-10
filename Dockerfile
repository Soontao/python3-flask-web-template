# run image
FROM python:3.7-slim

WORKDIR /app

# install dependency
RUN apt update
RUN apt install -y python-dev build-essential

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP app/app.py
ENV FLASK_ENV production

CMD ["flask", "run"]
