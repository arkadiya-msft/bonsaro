FROM python:3.7

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./health_checker.py .
COPY ./health_pb2_grpc.py .
COPY ./health_pb2.py .

ENTRYPOINT [ "python", "health_checker.py" ]
