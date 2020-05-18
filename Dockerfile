FROM python:3.8.3-slim
WORKDIR /code
COPY . /code/
RUN python -m pip install -r ./requirements.txt
CMD ["python", "./main.py"]
