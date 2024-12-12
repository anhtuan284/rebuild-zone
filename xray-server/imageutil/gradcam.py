"""
  Copyright 2024 LazySundayMorning

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
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras._tf_keras.keras.applications.densenet import preprocess_input
from keras._tf_keras.keras.preprocessing.image import img_to_array, array_to_img
from keras._tf_keras.keras.models import Model
from PIL import ImageDraw, ImageFont


def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    grad_model = Model(
        inputs=[model.input],
        outputs=[model.get_layer(last_conv_layer_name).output, model.output]
    )

    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]

    grads = tape.gradient(class_channel, last_conv_layer_output)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()


def display_gradcam(img, heatmap, alpha=0.5):
    heatmap = np.uint8(255 * heatmap)
    jet = plt.cm.get_cmap("jet")
    jet_colors = jet(np.arange(256))[:, :3]
    jet_heatmap = jet_colors[heatmap]
    jet_heatmap = array_to_img(jet_heatmap)
    jet_heatmap = jet_heatmap.resize((img.shape[1], img.shape[0]))
    jet_heatmap = img_to_array(jet_heatmap)
    superimposed_img = jet_heatmap * alpha + img
    superimposed_img = array_to_img(superimposed_img)
    return superimposed_img


def add_text_to_image(image, text, font_size=40):
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # Use Arial font if available
    except IOError:
        font = ImageFont.load_default()  # Fallback to default if Arial is not available

    # Set text position and color
    text_position = (20, image.height - 50)  # Adjusted position slightly higher
    text_color = (255, 255, 255)  # White text

    # Add the text to the image
    draw.text(text_position, text, fill=text_color, font=font)

    return image


def get_img_array_from_memory(img, size):
    img = img.resize(size)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)


def process_and_generate_images_from_memory(img, model, last_conv_layer_name, labels, top=3):
    img_array = get_img_array_from_memory(img, size=(224, 224))
    preds = model.predict(img_array)
    top_indices = preds[0].argsort()[-top:][::-1]

    images = []

    for index in top_indices[:3]:
        disease_name = labels[index]
        confidence = preds[0][index] * 100  # Convert to percentage

        # Generate heatmap
        heatmap = make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=index)

        # Generate Grad-CAM image
        superimposed_img = display_gradcam(img_to_array(img), heatmap)

        # Add disease name and confidence score to the image
        text = f"{disease_name}: {confidence:.2f}%"
        final_image = add_text_to_image(superimposed_img, text)

        images.append(final_image)

    return images
