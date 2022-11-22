FROM python:3.8

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py /app.py
COPY ./utils.py /utils.py
COPY /model.pkl /model.pkl

ENV PATH_TO_MODEL="/model.pkl"
ENV PATH_TO_DATA="data/data.csv"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]