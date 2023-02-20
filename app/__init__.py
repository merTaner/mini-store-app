from flask import Flask

app = Flask(__name__)

from app import views
from backend import orders_dao, product_dao

