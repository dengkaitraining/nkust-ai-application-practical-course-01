from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    #return send_file("index.html") #將 index.html送到Brower
    return app.send_static_file("index.html")

@app.route("/myimg")
def image():
    #return send_file("static/test.jpg", mimetype="image/jpeg")
    return app.send_static_file("test.jpg")

@app.route("/mydoc")
def docx():
    #return send_file("static/test.docx")
    return app.send_static_file("test.docx")
	
if __name__ == "__main__":
    app.run(debug=True) 