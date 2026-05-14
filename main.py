from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import io

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "message": "OCR API is working"
    })


@app.route("/ocr", methods=["POST"])
def ocr_image():
    try:
        if "image" not in request.files:
            return jsonify({
                "error": "No image uploaded"
            }), 400

        file = request.files["image"]

        image = Image.open(io.BytesIO(file.read()))

        text = pytesseract.image_to_string(image)

        return jsonify({
            "success": True,
            "text": text
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
