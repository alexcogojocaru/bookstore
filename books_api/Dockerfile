FROM python:3.8-slim-buster

WORKDIR .
COPY . .
RUN pip install -r requirements.txt
# RUN python add_data.py

CMD [ "python", "app.py" ]