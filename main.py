from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "helloworld"  # مجاني للتجربة


@app.route("/")
def home():
    return jsonify({
        "status": "running"
    })


@app.route("/ocr", methods=["POST"])
def ocr():
    try:
        if "image" not in request.files:
            return jsonify({
                "success": False,
                "error": "No image uploaded"
            })

        image = request.files["image"]

        response = requests.post(
            "https://api.ocr.space/parse/image",
            files={
                "filename": image.read()
            },
            data={
                "apikey": API_KEY,
                "language": "eng"
            }
        )

        result = response.json()

        parsed_text = result["ParsedResults"][0]["ParsedText"]

        return jsonify({
            "success": True,
            "text": parsed_text
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })


if __name__ == "__main__":
    app.run()
