from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def index():
	return stringReturn("helloworld")

def stringReturn(s):
	return s

if __name__ == '__main__':
	app.run(debug = True)
