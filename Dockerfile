FROM python:3.7.2

COPY WebInterface.py /
COPY templates/ /templates

RUN pip install Flask \
    wtforms \
    click

ENTRYPOINT [ "python" ]

CMD [ "./WebInterface.py" ]
