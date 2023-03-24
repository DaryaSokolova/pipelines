FROM python:3.10.2-buster
RUN pip install pandas

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# COPY requirements1.txt .
# RUN pip install --no-cache-dir -r requirements1.txt

# RUN poetry init
# ADD pipeline.py /
WORKDIR /example_pipeline
EXPOSE 8000
CMD [ "python", "pipeline.py" ]
WORKDIR /pipelines
COPY . .
# WORKDIR /example_pipeline