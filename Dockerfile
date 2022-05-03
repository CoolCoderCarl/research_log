FROM python:3.9-slim

WORKDIR /webapp

COPY requirements.txt /build/requirements.txt
COPY webapp.py /webapp
COPY templates/ /webapp/templates

RUN pip3.9 install -r requirements.txt

VOLUME /var/log/research_logs /webapp/research_logs

CMD [ "python3.9 /webapp/webapp.py" ]