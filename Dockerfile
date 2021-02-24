FROM python:3.7

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app

EXPOSE 80

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]