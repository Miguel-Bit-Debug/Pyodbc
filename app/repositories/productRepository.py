import json
from flask import jsonify
from ..db.db_config import config_db

class ProductRepository:
    def __init__(self):
        self.__db = config_db()

    def listProduct(self):
        products = self.__db.execute("Select * from Product").fetchall()

        dataResponse = []

        for product in products:
            dataResponse.append({"Id": product[0], "Name": product[1], "Description": product[2]})
        return {'result': dataResponse}

    def addProduct(self, product):
        self.__db.execute(f"insert into Product ([Name], [Description]) values('{product['name']}', '{product['description']}')")
        self.__db.commit()

        return True
    
    def getById(self, id):
        product = self.__db.execute(f"select * from Product where id = '{id}'").fetchone()
                
        return {"Id": product[0], "Name": product[1], "Description": product[2]}

    def updateProduct(self, id, product):
        self.__db.execute(f"update Product set [Name] = '{product['name']}', [Description] = '{product['description']}' where id = '{id}' ")

        self.__db.commit()

    def deleteProduct(self, id):
        self.__db.execute(f"delete from Product where id = '{id}' ")

        self.__db.commit()