from flask import Flask, render_template, request, jsonify
import base64
import cv2
import numpy as np
import pytesseract
import os
import time

app = Flask(__name__)

# Set Tesseract command
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Uncomment this line if you need to set TESSDATA_PREFIX in the code
# os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
@app.route('/recognize', methods=['POST'])
def recognize():
    try:
        data = request.get_json()
        image_data = data['image']
        
        if not image_data.startswith("data:image/png;base64,") and not image_data.startswith("data:image/jpeg;base64,"):
            return jsonify({"error": "Invalid image format"}), 400
        
        image_data = image_data.split(",")[1]
        image = base64.b64decode(image_data)
        
        np_image = np.frombuffer(image, np.uint8)
        img = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

        # Check if image is None
        if img is None:
            return jsonify({"error": "Failed to decode image"}), 400

        # Perform OCR
        text = pytesseract.image_to_string(img, lang='eng')
        print("Extracted Text:")
        print(text)

        # Create output folder if it doesn't exist
        output_folder = 'output'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Save output to file in output folder
        output_file = os.path.join(output_folder, f'output_{int(time.time())}.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)

        return jsonify({"message": "Image received and processed", "text": text})

    except Exception as e:
        print(f"Error: {e}")  # Print the error to the console
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
