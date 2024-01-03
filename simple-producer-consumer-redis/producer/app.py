from flask import Flask
import redis

channel = redis.Redis(
		host="localhost",
		port=6379,
	)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello producer"

@app.route('/redis')
def test_redis():
    return "Producer on" if (channel.ping()) else "error"

@app.route('/redis/<msg>')
def send_redis(msg):
    res = channel.lpush("app_queue", msg)
    return str(res)
