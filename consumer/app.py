from flask import Flask
import redis

channel = redis.Redis(
		host="redis",
		port=6379
	)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello anyone"

@app.route('/redis')
def test_redis():
    return "Consumer on" if (channel.ping()) else "error"

@app.route('/redis/consume')
def send_redis():
    res = channel.brpop("app_queue")
    return str(res)
