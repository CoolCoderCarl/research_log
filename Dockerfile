FROM python:3.7.9

COPY webapp.py /
COPY templates/ /templates
COPY requirements.txt requirements.txt

RUN pip3.7 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "./webapp.py" ]
