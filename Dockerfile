FROM docker.io/python:3.10

WORKDIR /

# --- [Install python and pip] ---
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3 python3-pip git
COPY . /

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

<<<<<<< HEAD
ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8086"
=======
ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8080"
>>>>>>> cd9b6ab947711db43868c515321e5c1f21ec4143

EXPOSE 8086

CMD [ "gunicorn", "main:app" ]