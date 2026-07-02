from flask import Flask
from logger import logger
from telegram import register

app = Flask(__name__)

logger.info("TURNX AI Director V5 starting...")

register(app)


@app.route("/", methods=["GET"])
def home():
    return "TURNX AI Director V5 is running!", 200


@app.route("/health", methods=["GET"])
def health():
    return {
        "status": "ok",
        "service": "TURNX AI Director V5"
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
