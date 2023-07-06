from flask import Flask, jsonify,request

app = Flask(__name__, template_folder='templates', static_folder='')
app.debug = True
data = None


@app.route("/api/getData",methods=["GET"])
def get_data():
	return ({"code": 200, "data": data}), 200

@app.route("/api/post",methods=["POST"])
def post():
	content_type = request.headers['Content-Type'].split(";")[0].strip()
	global data
	if content_type != 'application/json':
		raise TypeError("content_type只允许json格式")
	data = request.get_json()
	return jsonify({"code": 200, "msg": "success"}), 200


if __name__ == '__main__':
	app.run()

