FROM python:3.7.9

COPY webapp.py /
COPY templates/ /templates
COPY requirements.txt requirements.txt

RUN pip3.7 install -r requirements.txt

PORT 5000
VOLUME .logs_for_logs /logs_for_logs

ENTRYPOINT [ "python" ]

CMD [ "./webapp.py" ]
