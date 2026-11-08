
from flask import render_template, request, jsonify

from config import WORKSPACE_DIR
from app.services.file_service import FileService


file_service = FileService(WORKSPACE_DIR)


def register_routes(app):

    @app.route("/", methods=["GET"])
    def home():
        return render_template("index.html")

    @app.route("/api/files", methods=["POST"])
    def save_file():
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "Invalid JSON body"}), 400

        try:
            result = file_service.save_file(
                data.get("filename"),
                data.get("content")
            )
            return jsonify(result), 200

        except ValueError as error:
            return jsonify({"error": str(error)}), 400

        except OSError:
            return jsonify({"error": "Unable to save file"}), 500

    @app.route("/api/files", methods=["GET"])
    def open_file():
        filename = request.args.get("filename")

        try:
            result = file_service.open_file(filename)
            return jsonify(result), 200

        except ValueError as error:
            return jsonify({"error": str(error)}), 400

        except FileNotFoundError:
            return jsonify({"error": "File not found"}), 404

        except OSError:
            return jsonify({"error": "Unable to read file"}), 500
