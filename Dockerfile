FROM python:alpine AS base
MAINTAINER ANAND MUKHERJEE @ IfM


ADD . .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 12345

FROM base AS stage1

CMD [ "python3", "socket_push.py"]
