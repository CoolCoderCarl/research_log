FROM python:3

COPY WebInterface.py /
COPY templates/ /templates

RUN pip install Flask
RUN pip install wtforms
RUN pip install click

ENTRYPOINT [ "python" ]

CMD [ "./WebInterface.py" ]
