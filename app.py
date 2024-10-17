from flask import Flask, render_template, request, jsonify
import base64
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    data = request.get_json()
    image_data = data['image']
    
    # Remove the "data:image/png;base64," part
    image_data = image_data.split(",")[1]
    
    # Decode the image
    image = base64.b64decode(image_data)
    
    # Convert to numpy array and read it with OpenCV
    np_image = np.frombuffer(image, np.uint8)
    img = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
    
    # Here you can add your text recognition logic using Tesseract or any other library
    # For example:
    # text = pytesseract.image_to_string(img)

    # For demonstration, we'll just return a success message
    return jsonify({"message": "Image received and processed", "text": "Detected text goes here"})

if __name__ == '__main__':
    app.run(debug=True)
