import pymysql
import json
import base64
import pymysql.cursors

host = "localhost"
user = "root"
password = "vfczyz377283"
db_name = "shop"

def get_products_from_db():
    products = []
    try:
        connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected")

        try: 
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM `shoes`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    products.append(row)
        finally:
            connection.close()
    except Exception as e:
        print(f"Failed to get products from db: {e}")
        
    
    return json.dumps(products)



   