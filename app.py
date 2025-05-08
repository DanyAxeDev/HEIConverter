from flask import Flask, request, jsonify
from PIL import Image
import pillow_heif
import io
import base64

app = Flask(__name__)
pillow_heif.register_heif_opener()

@app.route('/converter', methods=['POST'])
def converter():
    data = request.get_json()
    base64_input = data.get("base64")

    if not base64_input:
        return jsonify({"error": "Base64 não fornecido"}), 400

    try:
        image_data = base64.b64decode(base64_input)

        image = Image.open(io.BytesIO(image_data))

        buffer = io.BytesIO()
        image.convert("RGB").save(buffer, format="JPEG")
        buffer.seek(0)

        jpeg_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        return jsonify({"jpegBase64": jpeg_base64}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)