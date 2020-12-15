from app import app
from flask import jsonify
import json
import sys

@app.route('/')
def index():
    return "bruh"

@app.route('/addItem', methods=['POST'])
def add_item():
    return jsonify({
        'status': 'bruh'
    })

@app.route('/removeItem', methods=['POST'])
def remove_item():
    return jsonify({
        'status': 'bruh'
    })

@app.route('/editItem', methods=['POST'])
def edit_item():
    return jsonify({
        'status': 'bruh'
    })

@app.route('/getItems', methods=['GET'])
def get_items():
    return jsonify({
        'status': 'bruh'
    })