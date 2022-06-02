from flask import Flask
from .routes.product import bp_product

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(bp_product)
    
    return app
