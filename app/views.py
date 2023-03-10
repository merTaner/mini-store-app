from app import app
from flask import request, jsonify, render_template, redirect
from backend import orders_dao, product_dao
import json

@app.route('/', methods=["GET", "POST"])
def getAllProductData():
    object_data = product_dao.getProduct()
    products_data = object_data.getProductData()
    
    return render_template("product.html", p_data=products_data)

@app.route('/insertdata', methods=["GET", "POST"])
def insertProductData():
    if request.method == "GET":
        return redirect("url_for('base')")
    else:
        data = request.json
        objectData = product_dao.getProduct()
        inserted_data = objectData.insertProductData(data)

        render_template("product.html")


@app.route('/update/<int:productid>', methods=["POST"])
def updateProductData(productid):
    data = request.json
    objectData = product_dao.getProduct()
    update_data = objectData.updateProduct(product_data=data, productid=productid)

    if update_data:
        response = jsonify({
            "status" :200,
            "message" : "successfully"
        })
    else:
        response = jsonify({
            "status" : 200,
            "message" : "faill"
        })
    
    return response

@app.route('/delete/<int:productid>', methods=["GET"])
def deleteProductData(productid):
    objectData = product_dao.getProduct()
    delete_data = objectData.deleteProduct(productid=productid)

    if delete_data != None:
        response = jsonify({
            "status" :200,
            "message" : "successfully"
        })
    else:
        response = jsonify({
            "status" : 200,
            "message" : "faill"
        })
    
    return response


@app.route('/orders')
def ordersData():
    object_data = orders_dao.getOrders()
    orders_data = object_data.getOrdersData()

    return orders_data

@app.route('/orderDetail', methods=["POST"])
def order_detail():
    object_data = orders_dao.getOrders()
    orderdetail = object_data.getOrderDetail(order_id=3)

    if orderdetail:
        response = jsonify({
            "status" :orderdetail,
            "message" : "successfully"
        })

    else:
        response = jsonify({
            "status" : 200,
            "message" : "faill"
        })
    
    return response 



@app.route('/addOrder', methods=["POST"])
def addOrder():
    data = {
            "customer_name" : "Mert Taner",
            "total": "500",
            "date":"20230204",
            "order_details": [
                {
                    'product_id': 1,
                    'amount': 5,     
                    'total_price': 70
                },
                {
                    'product_id': 2,
                    'amount': 5,       
                    'total_price': 60
                },
            ]
        }
    object_data = orders_dao.getOrders()
    insert_order = object_data.addOrder(order_data=data)

    if insert_order:
        response = jsonify({
            "status" :200,
            "message" : "successfully"
        })

    else:
        response = jsonify({
            "status" : 200,
            "message" : "faill"
        })
    
    return response

