FROM python:3.11.4

COPY . /db-handeller

WORKDIR /db-handeller

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "./main.py"]