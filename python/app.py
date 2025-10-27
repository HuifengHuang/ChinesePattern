from flask import Flask, send_file, send_from_directory, jsonify, request
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 存储图片的目录
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/images/<filename>')
def get_image(filename):
    """直接返回图片文件"""
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        return jsonify({'error': '文件不存在'}), 404

@app.route('/get-image-info')
def get_image_info():
    """返回图片信息，包含URL"""
    image_info = {
        'filename': 'example.jpg',
        'url': 'http://localhost:5000/images/example.jpg',
        'description': '示例图片'
    }
    return jsonify(image_info)

# 提供静态文件访问
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


@app.route('search')
def search():
    key_word = request.args.get('key_word')
    