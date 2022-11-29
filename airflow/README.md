# Airflow

## Build airflow-ml-base:
```bash
$ cd images/airflow-ml-base
$ docker build -t airflow-ml-base:latest .
```

## Reveal airflow:
```bash
$ export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
$ docker compose up --build
```

~~~
login: admin
password: admin
~~~
