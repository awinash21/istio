FROM python:3
WORKDIR /app
COPY . /app
RUN pip install flask
RUN pip install requests
EXPOSE 8000
EXPOSE 8002
CMD ["python","app.py"]
