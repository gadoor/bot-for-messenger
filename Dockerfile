FROM python:3.5
COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt
ENTRYPOINT python app.py
