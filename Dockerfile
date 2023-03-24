FROM python:3.10.2-buster
RUN pip install pandas

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY . .
EXPOSE 8000
CMD [ "python", "pipeline.py" ]