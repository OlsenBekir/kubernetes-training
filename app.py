from flask import Flask
import os
import socket
from datetime import datetime

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Bekir Kubernetes App")
APP_ENV = os.getenv("APP_ENV", "local")

should_fail = False

@app.route("/")
def index():
    return {
        "message": "Hei fra Kubernetes!",
        "app_name": APP_NAME,
        "environment": APP_ENV,
        "hostname": socket.gethostname(),
        "time": datetime.utcnow().isoformat() + "Z"
    }

@app.route("/health")
def health():
    if should_fail:
        return {"status": "error"}, 500
    return {"status": "ok"}

@app.route("/fail")
def fail():
    global should_fail
    should_fail = True
    return {"status": "failing"}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

