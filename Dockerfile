FROM python:3.12
RUN mkdir /fastapi_app
WORKDIR /fastapi_app
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
