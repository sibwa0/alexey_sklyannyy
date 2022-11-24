Build:
~~~
docker build -t skla00/online_model:s_2 .
~~~

Run:
~~~
docker run --rm -p 8000:8000 skla00/online_model:s_2
~~~

Pull:
~~~
docker pull skla00/online_model:s_2
~~~

Predict:
~~~
python make_request.py
~~~

Tests:
~~~
python -m unittest tests.py
~~~


Уменьшение размера образа docker:
1. Применил python:3.8-slim. Позволяется не загружать ненужные в данной задаче пакеты.
2. При установке пакетов указал --no-cache-dir, т.к. нет надобности кэшировать данные ведь повторная сборка образа происходит слишком часто, пакеты в любом случае приходится устанавливать заново.

Размер образа
    до: 1.34 Gb
    после: 0.557 Gb