from flask import Flask, send_from_directory, request
from PIL import Image
import base64
import io

MAX_IMG_SIZE_IN_BYTES = 100 * 1024
MAX_IMG_WIDTH = 640
MAX_IMG_HEIGHT = 640

app = Flask(__name__)


@app.get('/')
def send_report():
    return send_from_directory('.', 'index.html')


@app.post("/upload")
def hello_world():
    # TODO: set req size limit in Flask

    if "image_b64" not in request.json:
        return "Missing image_b64", 400

    image_base64 = request.json["image_b64"]

    if len(image_base64) > MAX_IMG_SIZE_IN_BYTES:
        return f"Image too large {len(image_base64) / 1024:.2f} KB", 400

    base64_decoded = base64.b64decode(image_base64)
    image = Image.open(io.BytesIO(base64_decoded))

    width, height = image.size
    if width > MAX_IMG_WIDTH or height > MAX_IMG_HEIGHT:
        return f"Image too wide or tall {width}x{height}", 400

    print(image)

    return "Got it", 200
