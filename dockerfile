FROM python:alpine

COPY ./setup.py /deploy/
COPY ./README.md /deploy/
COPY ./fairy_chess /deploy/fairy_chess
COPY ./tests /deploy/tests

WORKDIR /deploy


RUN apk add linux-headers
RUN apk add make musl-dev gcc postgresql-dev

RUN pip3 install -e .
RUN pip3 install pytest

EXPOSE 8000
CMD ["gunicorn", "--workers=3", "--worker-class=uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000", "fairy_chess:app"]