FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv ffmpeg

WORKDIR /app

RUN python3 -m venv venv

ENV PATH="/app/venv/bin:$PATH"

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python3", "service.py"]