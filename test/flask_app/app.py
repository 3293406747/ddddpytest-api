from flask import Flask, jsonify, request

app = Flask(__name__, template_folder='templates', static_folder='')
app.debug = True


@app.route("/api/getData", methods=["GET"])
def get_data():
	return jsonify({"code": 200, "msg": "success", "data": request.args}), 200


@app.route("/api/post", methods=["POST"])
def post():
	request_content_type = request.headers['Content-Type'].split(";")[0].strip()
	if request_content_type == 'application/json':
		return jsonify({"code": 200, "msg": "success", "data": request.get_json()}), 200
	return jsonify({"code": 200, "msg": "success"}), 200


if __name__ == '__main__':
	app.run()
