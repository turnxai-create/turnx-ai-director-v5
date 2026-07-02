from flask import Blueprint, request, jsonify
from logger import logger

telegram_bp = Blueprint("telegram", __name__)


@telegram_bp.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json(silent=True)

    logger.info(f"Telegram Update: {update}")

    return jsonify({
        "ok": True
    }), 200


def register(app):
    app.register_blueprint(telegram_bp)
