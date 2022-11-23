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
