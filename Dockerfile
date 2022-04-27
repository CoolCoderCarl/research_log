FROM python:3.7.9

WORKDIR /webapp

COPY webapp.py /
COPY templates/ /templates
COPY requirements.txt requirements.txt

RUN pip3.7 install -r requirements.txt

VOLUME .logs_for_logs /webapp/logs_for_logs

ENTRYPOINT [ "python" ]

CMD [ "./webapp.py" ]
