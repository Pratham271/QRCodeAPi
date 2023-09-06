from flask import Flask, jsonify, request
import qrcode
from io import BytesIO
from base64 import b64encode
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def generateQR():
    try:
        data = request.json.get('inputtext')
        
        if not data:
            return jsonify({'error': 'Missing inputtext parameter'}), 400
        
        memory = BytesIO()
        img = qrcode.make(data)
        img.save(memory)
        memory.seek(0)

        base64_img = "data:image/png;base64," + \
            b64encode(memory.getvalue()).decode('ascii')

        return jsonify({'qr_image': base64_img}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
