FROM python:3.5
COPY . /opt
WORKDIR /opt
RUN pip install requirements.txt
ENTRYPOINT python app.py
