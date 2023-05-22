from flask import request, Blueprint


router = Blueprint("api_router", __name__, url_prefix="/api")

@router.route('/suma', methods = ['GET'])
def sum():
	num1 = request.args.get('num1')
	num2 = request.args.get('num2')
	result = (int(num1) + int(num2)) if num1 and num2 else 0
	return {'result': result}
