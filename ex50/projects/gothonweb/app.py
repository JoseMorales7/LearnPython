import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    greeting = "Hello World!"
    return render_template("index.html", greeting=greeting)
    
if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    