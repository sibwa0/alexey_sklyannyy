FROM python:3.8-slim

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py /app.py
COPY ./utils.py /utils.py

ENV PATH_TO_MODEL="model.pkl"
ENV PATH_DOWNLOAD_MODEL="https://drive.google.com/uc?id=1GdSmk_5WWdys9wZhdtfI1ogY0xFm1C-H"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
