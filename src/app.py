from flask import Flask, request, render_template
from api import router
import json
import redis

channel = redis.Redis(
		host="redis",
		port=6379,
	)

app = Flask(__name__)



@app.route('/')
def hello_world():
    return "Hello anyone"

@app.route('/redis')
def test_redis():
    return "Consumer on" if (channel.ping()) else "error"

@app.route('/redis/<msg>')
def send_redis(msg):
    res = channel.lpush("app_queue", msg)
    return str(res)


@app.route('/template')
def template_test():
    return render_template('template.html')


@app.route('/user/<username>')
def show_user_profile(username):
    return f'{username}'

@app.route('/sum', methods = ['POST'])
def sum():
	data = json.loads(request.data)
	num1: int = data["num1"]
	num2: int = data["num2"]
	result = num1 + num2
	return ({'result': result})

@app.route('/template-2')
def template():
    return render_template('index.html', title='Anyone', user='Juan')

@app.route('/loop-template')
def loopTemplate():
    return render_template('loop.html', items=[1,2,4,2,4])

app.register_blueprint(router)

@app.errorhandler(404)
def page_not_found(error):
    return 'Not found', 404
