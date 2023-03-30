from connections import mysql

class getProduct(object):
    def __init__(self):
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()
    
    def getProductData(self):
        self.cursor.execute("SELECT * FROM PRODUCTS")
        product_data = self.cursor.fetchall()
        
        return product_data

    def insertProductData(self, unit_type, name, unit_price):

        self.cursor.execute("INSERT INTO PRODUCTS(UOM_ID, NAME, UNIT_PRICE) VALUES(%s,%s,%s);", (unit_type, name, unit_price))
        self.connection.commit()

        return self.cursor.rowcount
    
    def updateProduct(self, uom_type, name, unit_price, productid):

        self.cursor.execute("UPDATE PRODUCTS SET UOM_ID = '"+uom_type+"', NAME = '"+name+"', UNIT_PRICE = '"+unit_price+"' WHERE products_id = '"+str(productid)+"' ")
        self.connection.commit()

        return self.cursor.rowcount
    
    def deleteProduct(self, productid):
        self.cursor.execute(" DELETE FROM PRODUCTS WHERE PRODUCTS_ID = %s; " , (productid))
        self.connection.commit()

        return self.cursor.lastrowid

