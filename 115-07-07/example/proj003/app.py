from flask import Flask, send_file, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    #return send_file("index.html") #將 index.html送到Brower
    return app.send_static_file("index.html")

@app.route("/dynamic")
def dynamic():
    # 隨機生成一個 0 到 50 的數字，儲存到 dog 的變數中
    dog = random.randint(0, 50)
    print(dog)
    return render_template("locky.html", num = dog) # 將 dog 變數傳給 locky.html

@app.route("/myimg")
def image():
    #return send_file("static/test.jpg", mimetype="image/jpeg")
    return app.send_static_file("test.jpg")

@app.route("/mydoc")
def docx():
    #return send_file("static/test.docx")
    return app.send_static_file("test.docx")
	
if __name__ == "__main__":
    app.run(debug = True, port = 5010) 