FROM python:3.8-slim

LABEL org.opencontainers.image.source=https://github.com/yilbegan/telefuck

WORKDIR /app/
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/

CMD ["python", "-m", "app"]
