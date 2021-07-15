FROM python:3.8
LABEL maintainer="Preethi Narayan"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]