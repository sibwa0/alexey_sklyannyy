Build airflow-ml-base:
~~~
cd images/airflow-ml-base
docker build -t airflow-ml-base:latest .
~~~

# для корректной работы с переменными, созданными из UI
Reavel airflow:
~~~
export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
docker compose up --build
~~~
