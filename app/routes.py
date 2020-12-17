# -*- coding: utf-8 -*-

from app import app, db
from flask import jsonify, request
import json
import sys

from app.models import Item, Receipe

@app.route('/addItem', methods=['POST'])
def add_item():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    item_name = post_data.get('item_name')
    quantity = post_data.get('quantity', 0)
    unit = post_data.get('unit', '')
    item = Item(item_name=item_name, quantity=quantity, unit=unit)
    db.session.add(item)
    db.session.commit()
    return jsonify(response_object)


@app.route('/removeItem', methods=['POST'])
def remove_item():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    item_id = int(post_data.get('id'))
    Item.query.filter(Item.id == item_id).delete()
    db.session.commit()
    return jsonify(response_object)


@app.route('/editItem', methods=['POST'])
def edit_item():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    item_name = post_data.get('item_name')
    quantity = post_data.get('quantity', 0)
    unit = post_data.get('unit', '')
    item_id = post_data.get('id')

    item = Item.query.filter(id=item_id).first()

    item.item_name = item_name
    item.quantity = quantity
    item.unit = unit

    db.session.commit()
    return jsonify(response_object)


@app.route('/getItems', methods=['GET'])
def get_items():
    response_object = {'status': 'success'}
    items = Item.query.all()
    return jsonify([item.serialize for item in items])