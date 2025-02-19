from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return f"<h1>Wild Rydes</h1><p>Developed by: Zafar Pathan</p><p>Company ID: 100946341</p>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000) # Host 0.0.0.0 for containerization
