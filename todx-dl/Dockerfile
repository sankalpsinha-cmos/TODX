FROM python:3.11.4

COPY . /todx-dl

WORKDIR /todx-dl

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "./main.py"]