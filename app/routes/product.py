from flask import Blueprint, request, jsonify, Response
from ..services.productService import ProductService

bp_product = Blueprint('product', __name__)

productService = ProductService()

@bp_product.route('/', methods=['GET'])
def index():
    products = productService.listProducts()

    return products

@bp_product.route('/<id>', methods=['GET'])
def getById(id):
    product = productService.getById(id)

    return product

@bp_product.route('/', methods=['POST'])
def add():
    product = request.json
    productService.addProduct(product)
    return product
        
@bp_product.route('/<id>', methods=['PUT'])
def update(id):
    product = request.json

    productService.updateService(id, product)
    
    return product

    
@bp_product.route('/<id>', methods=['DELETE'])
def delete(id):
    productService.deleteService(id)
    
    return "Deleted"