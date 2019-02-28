FROM python:3.5
ADD . /app
WORKDIR app
RUN pip install -r requirements/develop.txt

ENTRYPOINT ["python", "src/core.py"]