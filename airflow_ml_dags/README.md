# Airflow
Implement following steps:

### 1. Build airflow-ml-base:
```bash
$ cd images/airflow-ml-base
$ docker build -t airflow-ml-base:latest .
```

### 2. Reveal airflow:
```bash
$ export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
$ export PATH_VOLUME=$(pwd)/data

from airflow_ml_dags run:
$ docker compose up --build
```

### 3. Open in browser
~~~
http://localhost:8080/

login: admin
password: admin
~~~
