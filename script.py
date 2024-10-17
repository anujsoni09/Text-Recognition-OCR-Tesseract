import pytesseract
from PIL import Image
import os

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Specify the path to the image file you want to process
image_path = 'sample1.png'  # Change this to your image file path

# Load the image
image = Image.open(image_path)

# Perform OCR on the image
# Replace 'eng' with the language code you want to use (e.g., 'spa' for Spanish)
text = pytesseract.image_to_string(image, lang='eng')

# Print the extracted text
print("Extracted Text:")
print(text)

# Optionally, save the text to a file
output_file = 'output.txt'  # Change this if you want a different output file name
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Text saved to {output_file}")
