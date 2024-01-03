from flask import Flask
import redis

channel = redis.Redis(
		host="localhost",
		port=6379,
        decode_responses=True
	)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello consumer"

@app.route('/redis')
def test_redis():
    return "Consumer on" if (channel.ping()) else "error"

@app.route('/redis/consume')
def send_redis():
    res = channel.brpop(keys=["app_queue"])
    return str(res)
