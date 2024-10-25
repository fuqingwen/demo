FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt

CMD ["python", "main.py"]