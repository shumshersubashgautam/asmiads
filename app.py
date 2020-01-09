from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home_func():
	return render_template("index.html")

@app.route("/uploadfiles",methods=["GET","POST"])
def upload_files():
	return render_template("uploadfiles.html")

if __name__ == 'main' :
	app.run()
