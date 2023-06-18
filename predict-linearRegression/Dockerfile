FROM python:latest
COPY requirements.txt .
RUN pip install --quiet -r requirements.txt

COPY predict.py .
CMD python predict.py