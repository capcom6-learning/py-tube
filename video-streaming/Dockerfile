FROM python:3.9-alpine as prod

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./base.py" ]

FROM python:3.9 as dev

WORKDIR /app

CMD pip install -r requirements.txt && \
    watchgod base.main
