from flask import Flask, send_file, send_from_directory, jsonify, request
import os
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

# 存储图片的目录
# UPLOAD_FOLDER = 'D:\RA工作目录\code workspace\ChinesePattern\python'
UPLOAD_FOLDER = 'E:\kangziyao\CodingSapce\ChinesePattern\python'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/images/<filename>')
def get_image(filename):
    """直接返回图片文件"""
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'] + '\images', filename + '.png')
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


@app.route('/search', methods=['POST'])
def search():
    req = request.get_json()
    key_word = req['key_word']
    print(key_word)
    results = []
    with open(UPLOAD_FOLDER + '\Chinese Pattern.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for value in row.values():
                if key_word in value:
                    results.append(row)
                    break
    print(results)
    return jsonify(results)


@app.route('/all_cards')
def all_cards():
    results = []
    with open(UPLOAD_FOLDER + '\Chinese Pattern.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['fileName'] is not "":
                results.append(row)
    print(results)
    return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
