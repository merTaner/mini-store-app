from connections import mysql

class getOrders(object):
    def __init__(self):
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()

    def getOrdersData(self):
        self.cursor.execute(" SELECT * FROM ORDERS; ")
        order_data = self.cursor.fetchall()

        response = []

        for (order_id, customer_name, total, date) in order_data:
            response.append({
                "order_id" : order_id,
                "customer_name" : customer_name,
                "total" : total,
                "date" : date,
            })

        return response
    
    def addOrder(self, order_data):
        # add order
        customer_name = order_data["customer_name"]
        total = order_data["total"]
        date = order_data["date"]

        self.cursor.execute("INSERT INTO ORDERS(CUSTOMER_NAME, TOTAL, DATE) VALUES(%s,%s,%s);", (customer_name, total, date))
        
        # order detail 
        order_id = self.cursor.lastrowid

        order_details_query = ("INSERT INTO order_details"
                           "(order_id, product_id, amount, total_price)"
                           "VALUES (%s, %s, %s, %s)")

        order_details_data = []
        for order_detail_record in order_data['order_details']:
            order_details_data.append([
                order_id,
                int(order_detail_record['product_id']),
                float(order_detail_record['amount']),
                float(order_detail_record['total_price'])
            ])
        self.cursor.executemany(order_details_query, order_details_data)

        self.connection.commit()

        return order_id

        
    
    def getOrderDetail(self, order_id):
        query = "SELECT * from order_details where order_id = %s"

        query = "SELECT order_details.order_id, order_details.amount, order_details.total_price, "\
            "products.name, products.unit_price FROM order_details LEFT JOIN products on " \
            "order_details.product_id = products.products_id where order_details.order_id = %s"

        data = (order_id, )

        self.cursor.execute(query, data)

        records = []
        for (order_id, amount, total_price, product_name, unit_price) in self.cursor:
            records.append({
                'order_id': order_id,
                'amount': amount,
                'total_price': total_price,
                'product_name': product_name,
                'unit_price': unit_price
            })

        self.cursor.close()

        return records      




