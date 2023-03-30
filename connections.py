from flaskext.mysql import MySQL
from app import app

mysql = MySQL()

app.config["MYSQL_DATABASE_HOST"] = "127.0.0.1"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "20011002"
app.config["MYSQL_DATABASE_DB"] = "gs_app"

mysql.init_app(app)