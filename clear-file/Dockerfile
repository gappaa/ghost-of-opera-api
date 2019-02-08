FROM python

ENV FLASK_APP=clear_api.py
ENV HOST=0.0.0.0
ENV PORT=6789
ENV APP_INI_FILE=./ini/config.ini

WORKDIR /usr/src/app
COPY ./requirements.txt ./requirements.txt
RUN pip install --user -r requirements.txt
COPY . .

CMD ["./run.sh"]

