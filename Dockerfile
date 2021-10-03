FROM python:3.8

RUN mkdir -p /home/evgenia/PycharmProjects/app/
WORKDIR /home/evgenia/PycharmProjects/app/

COPY . /home/evgenia/PycharmProjects/app/
ADD requirements.txt /home/evgenia/PycharmProjects/app/requirements.txt
RUN pip install -r /home/evgenia/PycharmProjects/app/requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]