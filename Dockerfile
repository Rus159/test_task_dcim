FROM python:3.8-alpine

RUN adduser -D task

WORKDIR /home/task

COPY requirments.txt requirments.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirments.txt
RUN venv/bin/pip install gunicorn

COPY migrations migrations
COPY templates templates
COPY decorators.py api.py app.py config.py extensions.py models.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP app.py

RUN chown -R task:task ./
USER task

EXPOSE 5005

ENTRYPOINT ["./boot.sh"]
