import json

from flask import request, Blueprint


api = Blueprint("api", __name__, url_prefix="/api")


@api.route('/sum', methods = ['GET', 'POST'])
def sum():
	num1, num2 = 0, 0
	if request.method == 'POST':
		data = json.loads(request.data)
		num1 = data["num1"]
		num2 = data["num2"]
	elif request.method == 'GET':
		num1 = request.args.get('num1')
		num2 = request.args.get('num2')
	result = (int(num1) + int(num2)) if num1 and num2 else 0
	return {'result': result}