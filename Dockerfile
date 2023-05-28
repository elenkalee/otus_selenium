# Устанавка базового образ
FROM python:3.11-alpine
WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest"]



