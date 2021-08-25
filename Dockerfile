FROM python:3.8

WORKDIR /usr/src/minduo

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/minduo/requirements.txt

RUN pip install -U pip --no-cache-dir && \
    pip install --no-cache-dir wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /usr/src/minduo/entrypoint.sh

COPY ./src /usr/src/minduo/src

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]