FROM python:3.12-slim
WORKDIR /app
RUN pip install pandas
COPY data_cleaner_test.py .
COPY 03_LibrarySystembook.csv .
ENTRYPOINT ["python", "data_cleaner_test.py"]
