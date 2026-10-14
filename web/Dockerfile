FROM python:3.14-slim
MAINTAINER Chris Warner "cbwar@uoregon.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
