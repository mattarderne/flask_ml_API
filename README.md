# flask_ml_API
Flask API test
> Test POC for end to end Machine Learning API development
1. Train model, 
2. Pickle, 
3. Publish as endpoint API

To start, run `python service.py`
and then go to `http://127.0.0.1:5000/?text=Windows%20is%20a%20operating%20system` 

# links
[building-a-text-classifier-using-python-and-docker](https://medium.com/@mattvonrohr/from-dev-to-ops-building-a-text-classifier-using-python-and-docker-part-3-building-a-web-911d88477989

[flask docker tutorial](https://runnable.com/docker/python/dockerize-your-flask-application)

# venv
```shell
python3 -m venv  ~/.virtualenvs/flask
source ~/.virtualenvs/flask/bin/activate
pip install flask
pip install sklearn
flask run
```

& then go to `http://127.0.0.1:5000/?text=Windows%20is%20a%20operating%20system` 

# docker

```shell
docker build -t test/text-classifier-service .
docker run -it --rm -p 5000:5000 test/text-classifier-service
```

& then go to `http://127.0.0.1:5000/?text=Windows%20is%20a%20operating%20system` 