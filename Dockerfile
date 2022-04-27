FROM python:3.7.9

WORKDIR /webapp

COPY webapp.py /webapp
COPY templates/ /webapp/templates
COPY requirements.txt /webapp/requirements.txt

RUN pip3.7 install -r requirements.txt

VOLUME .logs_for_logs /webapp/logs_for_logs

ENTRYPOINT [ "python" ]

CMD [ "./webapp.py" ]
