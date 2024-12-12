"""
Copyright (c) 2024 LazySundayMorning

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import io
import os
import zipfile
import base64
import cloudinary.uploader
import imageutil
import sentry_sdk

from sympy.printing.tensorflow import tensorflow
from dotenv import load_dotenv

from flask_cors import CORS
from flask import Flask, request, send_file, jsonify
from ultralytics import YOLO
from PIL import Image

load_dotenv()

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DNS"),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    _experiments={
        # Set continuous_profiling_auto_start to True
        # to automatically start the profiler on when
        # possible.
        "continuous_profiling_auto_start": True,
    },
)

app = Flask(__name__)
CORS(app)

# Load models
yolo_model = YOLO('models/best.pt')
densenet_model = tensorflow.keras.models.load_model('models/DenseNet121_epoch_30.keras')


class CFG:
    CLASS_NAMES = [
        "Atelectasis",
        "Cardiomegaly",
        "Effusion",
        "Infiltration",
        "Mass",
        "Nodule",
        "Pneumonia",
        "Pneumothorax",
        "Consolidation",
        "Edema",
        "Emphysema",
        "Fibrosis",
        "Pleural_Thickening",
        "Hernia",
    ]
    LAST_CONV_LAYER = 'conv5_block16_concat'


def load_image_from_request(request_file):
    """Load image from incoming request."""
    img_bytes = request_file.read()
    return Image.open(io.BytesIO(img_bytes)).convert("RGB")


def load_image_from_base64(base64_str):
    """Convert Base64 string to PIL Image."""
    img_data = base64.b64decode(base64_str)
    return Image.open(io.BytesIO(img_data)).convert("RGB")


def upload_image_to_cloudinary(image):
    """Upload image to Cloudinary and return the URL."""
    img_buffer = io.BytesIO()
    image.save(img_buffer, format='JPEG')
    img_buffer.seek(0)

    # Upload to Cloudinary
    upload_response = cloudinary.uploader.upload(img_buffer, folder="rebuildzone")
    return upload_response['secure_url']


def save_image_to_memory(image, fmt='JPEG'):
    """Save image to a BytesIO memory buffer."""
    img_buffer = io.BytesIO()
    image.save(img_buffer, format=fmt)
    img_buffer.seek(0)
    return img_buffer


def create_zip_from_images(images):
    """Create a ZIP archive from a list of images in-memory."""
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for i, img in enumerate(images):
            img_buffer = save_image_to_memory(img)
            zip_file.writestr(f'image_{i}.jpg', img_buffer.getvalue())
    zip_buffer.seek(0)
    return zip_buffer


@app.route('/yolo_predict', methods=['POST'])
def yolo_predict():
    img = load_image_from_request(request.files['image'])
    results = yolo_model.predict(img, imgsz=640)
    img_with_boxes = Image.fromarray(results[0].plot())  # Convert result to PIL Image
    img_buffer = save_image_to_memory(img_with_boxes)

    return send_file(img_buffer, mimetype='image/jpeg')


@app.route('/densenet_predict', methods=['POST'])
def densenet_predict():
    img = load_image_from_request(request.files['image'])
    images = imageutil.process_and_generate_images_from_memory(
        img, densenet_model, CFG.LAST_CONV_LAYER, CFG.CLASS_NAMES
    )
    zip_buffer = create_zip_from_images(images)

    return send_file(
        zip_buffer,
        mimetype='application/zip',
        as_attachment=True,
        download_name='grad_cam_images.zip'
    )
@app.route('/v2/yolo_predict', methods=['POST'])
def yolo_predict_v2():
    """
    New YOLO prediction API that uploads processed image to Cloudinary.
    """
    base64_str = request.json.get('image')  # Get Base64 string from JSON body
    img = load_image_from_base64(base64_str)

    results = yolo_model.predict(img, imgsz=640)
    img_with_boxes = Image.fromarray(results[0].plot())  # Convert result to PIL Image

    # Upload image to Cloudinary and return URL
    image_url = upload_image_to_cloudinary(img_with_boxes)

    return jsonify({"image_url": image_url})


@app.route('/v2/densenet_predict', methods=['POST'])
def densenet_predict_v2():
    """
    New DenseNet prediction API that uploads processed Grad-CAM images to Cloudinary.
    """
    base64_str = request.json.get('image')  # Get Base64 string from JSON body
    img = load_image_from_base64(base64_str)

    images = imageutil.process_and_generate_images_from_memory(
        img, densenet_model, CFG.LAST_CONV_LAYER, CFG.CLASS_NAMES
    )

    # Upload images to Cloudinary
    image_urls = [upload_image_to_cloudinary(image) for image in images]

    # Join URLs with comma and return as a single string
    image_urls_string = ",".join(image_urls)
    print(image_urls_string)

    return jsonify({"image_urls": image_urls_string})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)