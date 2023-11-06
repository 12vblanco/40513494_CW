import sqlite3
from flask import jsonify
from app import app

# I created the route for the API in a separate file for clarity

@app.route('/bookings_API')
def bookings_api():    
    con = sqlite3.connect('bookings.db')
    cur = con.cursor()
    
    cur.execute("SELECT * FROM bookings")
    bookings = cur.fetchall()
    con.close()
    
    # extracted from https://stackoverflow.com/questions/66367271/displaying-a-list-of-data-from-in-flask-rest-api-python
    # and from the serendipity chapter in the projectBook.pdf
    
    # empty list to collect the list of dictionaries
    data_list = []
    
    # a loop to extract each field from each entry
    for booking in bookings:
        data = {
            "_id" : booking[0],
            "name" : booking[1],
            "email" : booking[2],
            "date" : booking[3],
            "time" : booking[4],
            "table" : booking[5]
            }
        
        # add the results to the empty list
        data_list.append(data)
    # convert the result into a json response with josonify
    return jsonify(data_list), 200

# to check the API is working: https://127.0.0.1:5000/bookings_API