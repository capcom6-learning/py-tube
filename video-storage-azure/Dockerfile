FROM python:3.9-alpine AS base

FROM base AS build

# We need to build cffi, so we will use multi-stage build
RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev

WORKDIR /app
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

FROM base AS prod
WORKDIR /app

COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY . .

CMD [ "python", "-u", "./base.py" ]

FROM python:3.9 AS dev
WORKDIR /app

CMD pip install -r requirements.txt && \
    pip install watchgod && \
    watchgod base.main --args -u

