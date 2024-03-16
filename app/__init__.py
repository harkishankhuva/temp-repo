from flask import Flask, request

app = Flask(__name__)

@app.route("/division")
def do_division():
	a, b = request.args.get('a'), request.args.get('b')
	a, b = map(float, [a,b])
	return str(a/b)

