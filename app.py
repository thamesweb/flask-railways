import pandas as pd
import numpy as np
import PIL
import pickle
import os
import tensorflow as tf
import joblib
import imghdr
from bson.binary import Binary
from flask import Flask, request, jsonify, send_file
from flask_pymongo import pymongo
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as image_utils
from dotenv import load_dotenv
from io import BytesIO
from bson.objectid import ObjectId


load_dotenv()
# Declare a Flask app
app = Flask(__name__)

# MongoDB Connection
# client = None
client = pymongo.MongoClient(os.getenv('MONGODB_URI'))
db = client.get_database('uploaded_image') if client else None 

# Model Classes
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# Model Prediction
def predict(model, img):
    test_img = image_utils.load_img(img, target_size=(256, 256))
    img_arr = image_utils.img_to_array(test_img)
    img_arr = tf.expand_dims(img_arr ,0)

    prediction = model.predict(img_arr)

    predicted_class = class_names[np.argmax(prediction[0])]
    confidence = round(100 *(np.max(prediction[0])),2)

    return predicted_class , confidence

# Get Image from DB
@app.route('/image/<image_id>', methods=['GET'])
def get_image(image_id):
    image = db.images.find_one({"_id": ObjectId(image_id)})
    if image is None:
        return jsonify({'message': 'Image not found', 'success':'false'}), 404
    else:
        image_data = image['image']
        image_format = image['format']
        return send_file(BytesIO(image_data), mimetype=('image/'+image_format))

# Get and Post Request handler
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return jsonify({'status': 'active', 'message': 'Waste AI'}), 200
    elif request.method == 'POST':
        image = request.files['image']  # fet input
        image_data = Binary(image.read())
        image_format = imghdr.what(None, h=image_data)
        if db is None:
            return jsonify({'success': 'false', 'message': 'DB not Connected'})
        else:
            alreadyInDB = db.images.find_one({"image": image_data})  # check if image already exists in database
            if alreadyInDB is None:
                image_id = db.images.insert_one({"image": image_data, "format":image_format}).inserted_id
            else:
                image_id = alreadyInDB['_id']

        model =load_model("vgg16_model.h5")
        predicted_class , confidence = predict(model, BytesIO(image_data))
        return jsonify(
            {
                'success': 'true',
                'message': 'Prediction Successful',
                'prediction': predicted_class,
                'confidence': confidence,
                'image_id': str(image_id),
            }
        )
        

# Running the app
if __name__ == '__main__':
    app.run(debug = True)