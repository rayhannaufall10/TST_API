import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "tst_house",
    )

db_cursor = mydb.cursor()

# @app.get("/greet")
# def index():
#     return jsonify(db_cursor.fetchall())

@app.route("/view", methods=["GET"])
def read():
    db_cursor.execute("SELECT * FROM melb_data")
    return jsonify(db_cursor.fetchall())

@app.route("/add", methods=["POST"])
def create():
    db_cursor.execute("INSERT INTO melb_data (suburb, address, rooms, price, seller, date, distance, bedroom, bathroom, car, landsize) \
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (request.json["suburb"], request.json["address"], request.json["rooms"], request.json["price"], request.json["seller"], 
                       request.json["date"], request.json["distance"], request.json["bedroom"],
                       request.json["bathroom"], request.json["car"], request.json["landsize"]))
    mydb.commit()
    return jsonify({"Message" : "House Succesfully Added"})

@app.route("/updatePrice", methods=["PUT"])
def update():
    db_cursor.execute("UPDATE melb_data SET price = %s WHERE address = %s", (request.json["price"], request.json["address"]))
    mydb.commit()
    return jsonify({"Message" : "House Succesfully Updated"})

@app.route("/delete", methods=["DELETE"])
def delete():
    db_cursor.execute("DELETE FROM melb_data WHERE address = %s", (request.json["address"],))
    mydb.commit()
    return jsonify({"Message" : "House Succesfully Deleted"})

if __name__ == "__main__":
    app.run(debug = True)