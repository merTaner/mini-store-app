from app import app
from flask import request, jsonify, render_template, redirect, url_for
from backend import orders_dao, product_dao
import json
from datetime import datetime

@app.route('/', methods=["GET", "POST"])
def getAllProductData():
    object_data = product_dao.getProduct()
    products_data = object_data.getProductData()
    
    return render_template("product.html", p_data=products_data)

@app.route('/insertdata', methods=["POST"])
def insertProductData():
    uom_type = request.form['uom_type']
    name = request.form['name']
    unit_price = request.form['unit_price']

    objectData = product_dao.getProduct()
    inserted_data = objectData.insertProductData(uom_type, name, unit_price)

    return redirect(url_for('getAllProductData'))


@app.route('/update', methods=["POST"])
def updateProductData():
    product_id = request.form['prduct_id'] 
    uom_type = request.form['uom_type']
    name = request.form['name']
    unit_price = request.form['unit_price']

    objectData = product_dao.getProduct()
    update_data = objectData.updateProduct(uom_type=uom_type, name=name, unit_price=unit_price, productid=product_id)

    return redirect(url_for('getAllProductData'))



@app.route('/delete/<int:productid>', methods=["GET"])
def deleteProductData(productid):
    objectData = product_dao.getProduct()
    delete_data = objectData.deleteProduct(productid=productid)

    return redirect(url_for('getAllProductData'))


@app.route('/orders')
def ordersData():
    object_data = orders_dao.getOrders()
    orders_data = object_data.getOrdersData() 
    
    product_object = product_dao.getProduct()
    product_data = product_object.getProductData()

    return render_template('order.html', o_data = orders_data, product_data = product_data)

@app.route('/addOrder', methods=["GET", "POST"])
def addOrder():
    if request.method == "GET":
        return render_template('order.html')
    else:
        data = {
                "customer_name" : request.form['customer_name'],
                "total": request.form['total_price'],
                "date": datetime.now(),
                "order_details": [
                    {
                        'product_id': request.form['product_id'],
                        'amount': request.form['amount'],
                        'total_price': request.form['total_price']
                    },
                ]
            }
        object_data = orders_dao.getOrders()
        insert_order = object_data.addOrder(order_data=data)

        return redirect(url_for('ordersData'))

@app.route('/orderDetail/<int:order_id>', methods=["GET", "POST"])
def order_detail(order_id):
    if request.method == "GET":
        object_data = orders_dao.getOrders()
        orderdetail = object_data.getOrderDetail(order_id)

        return render_template('order_detail.html', order_detail_data = orderdetail)
    else:
        return render_template('order_detail.html')

