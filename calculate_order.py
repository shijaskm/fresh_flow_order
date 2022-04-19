import sqlite3
import itertools
from flask import Flask, jsonify, request


db_file = "C:/Users/shijas/Downloads/data.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("Error connection")
    return conn

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def order_fun():
    if (request.method == 'GET'):
        conn = create_connection(db_file)
        cur = conn.cursor()
        order_items = cur.fetchall()
        #print(order_items)
        #print(type(order_items))

        ord = cur.execute("SELECT oi.item_number,ordering_day,delivery_day,suggested_retail_price,profit_margin,purchase_price,item_categories,tags,    case_content_quantity,case_content_unit,(sp.sales_quantity-i.inventory)/oi.case_content_quantity as order_quantity,'CS' as unit,i.inventory as      inventory_quantity FROM orderable_items oi left outer join sales_predictions sp on oi.item_number = sp.item_number and oi.ordering_day =    substr(sp.day,1,10) left outer join inventory i  on oi.item_number = i.item_number and oi.ordering_day = substr(i.day,1,10)")
        ord_data = []
        for row in ord:
            order = {"item_number": row[0], "ordering_day": row[1], "delivery_day": row[2],"suggested_retail_price":  row[3],"profit_margin":  row[4],  "purchase_price":  row[5],"item_categories":  row[6],"tags":  row[7],"case_content_quantity":  row[8],"case_content_unit":  row[9],"order_quantity":    row[10],"unit":  row[11],"inventory_quantity":  row[12]}
            ord_data.append(order)

        print(ord_data)
        return jsonify({'data': ord_data})


if __name__ == '__main__':
    app.run(debug=True)