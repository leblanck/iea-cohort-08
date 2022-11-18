FROM python:3.8-alpine
COPY . /app
RUN pip3 install --user -r /app/requirements.txt
EXPOSE 8080
CMD python3 /app/app.py