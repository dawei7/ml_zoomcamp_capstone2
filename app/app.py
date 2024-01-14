from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = tf.keras.models.load_model('mnist_model.h5')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            image = Image.open(io.BytesIO(file.read())).convert('L')
            image = image.resize((28, 28))
            image = np.array(image)
            image = np.invert(image)  # Invert the image colors
            image = image / 255.0
            image = image.reshape(1, 28, 28)
            
            prediction = model.predict(image)
            digit = np.argmax(prediction)
            probability = np.max(prediction)
            
            return f'Predicted Digit: {digit} with probability {probability:.2f}'
    
    return '''
    <!doctype html>
    <title>Upload Image</title>
    <h1>Upload a Digit Image</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
