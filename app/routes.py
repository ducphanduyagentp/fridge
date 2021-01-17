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
    ingredient_type = post_data.get('ingredient_type', '')
    item = Item(item_name=item_name, quantity=quantity, unit=unit, ingredient_type=ingredient_type)
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
    ingredient_type = post_data.get('ingredient_type', '')
    item_id = int(post_data.get('id'))

    item = Item.query.filter(Item.id == item_id).first()

    item.item_name = item_name
    item.quantity = quantity
    item.unit = unit
    item.ingredient_type = ingredient_type

    db.session.commit()
    return jsonify(response_object)


@app.route('/getItems', methods=['GET'])
def get_items():
    response_object = {'status': 'success'}
    items = Item.query.all()
    return jsonify([item.serialize for item in items])


@app.route('/getReceipes', methods=['GET'])
def get_receipes():
    respose_object = {'status': 'success'}
    receipes = Receipe.query.all()
    return jsonify([receipe.serialize for receipe in receipes])


@app.route('/addReceipe', methods=['POST'])
def add_receipe():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    receipe_name = post_data.get('receipe_name')
    ingredients = post_data.get('ingredients', [])
    cooking_time = int(post_data.get('cooking_time', 0))
    optional_ingredients = post_data.get('optional_ingredients', [])
    receipe = Receipe(receipe_name=receipe_name, ingredients=ingredients, cooking_time=cooking_time, optional_ingredients=optional_ingredients)
    db.session.add(receipe)
    db.session.commit()
    return jsonify(response_object)


@app.route('/removeReceipe', methods=['POST'])
def remove_receipe():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    receipe_id = int(post_data.get('id'))
    Receipe.query.filter(Receipe.id == receipe_id).delete()
    db.session.commit()
    return jsonify(response_object)


@app.route('/editReceipe', methods=['POST'])
def edit_receipe():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    receipe_name = post_data.get('receipe_name')
    ingredients = post_data.get('ingredients', [])
    cooking_time = post_data.get('cooking_time', 0)
    optional_ingredients = post_data.get('optional_ingredients', [])
    receipe_id = int(post_data.get('id'))

    receipe = Receipe.query.filter(Receipe.id == receipe_id).first()

    receipe.receipe_name = receipe_name
    receipe.ingredients = ingredients
    receipe.cooking_time = cooking_time
    receipe.optional_ingredients = optional_ingredients

    db.session.commit()
    return jsonify(response_object)
