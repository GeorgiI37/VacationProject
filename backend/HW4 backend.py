import flask
import mysql.connector
from mysql.connector import Error
from flask import jsonify
from flask import request, make_response
from flask_cors import CORS
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#creating connection to mysql database
conn = create_connection('cis3368.c2sn9hhzxonj.us-east-1.rds.amazonaws.com', 'ceharp', 'jackson1', 'CIS3368db')
# conn = create_connection('localhost', 'root', '', 'CIS3368db')


#setting up an application name
app = flask.Flask(__name__) #sets up the application
CORS(app)
app.config['DEBUG'] = False #shows errors in browser

def connect_db() : 
    conn = create_connection('cis3368.c2sn9hhzxonj.us-east-1.rds.amazonaws.com', 'ceharp', 'jackson1', 'CIS3368db')

#api to get all values from the trip table
@app.route('/api/trips', methods=['GET'])
def get_trips():
    #selects all values from the trip table
    print('api/trips')
    
    conn = create_connection('cis3368.c2sn9hhzxonj.us-east-1.rds.amazonaws.com', 'ceharp', 'jackson1', 'CIS3368db')

    sql = 'SELECT * FROM trips JOIN destinations ON trips.destination_id = destinations.destination_id'
    # cursor = conn.cursor()
    # cursor.execute(sql)
    # result = cursor.fetchall()
    com = execute_read_query(conn, sql)
    return jsonify(com)

@app.route('/api/trips/<id>', methods=['GET'])
def get_trip(id):
    #select value from the trip table
    print('api/trips/', id)
    conn = create_connection('cis3368.c2sn9hhzxonj.us-east-1.rds.amazonaws.com', 'ceharp', 'jackson1', 'CIS3368db')
    sql = 'SELECT * FROM trips WHERE trip_id = ' + id
    com = execute_read_query(conn, sql)
    return jsonify(com)

@app.route('/api/trips/delete/<id>', methods=['GET'])
def delete_trips(id):
    #delete value from the trip table
    print('api/trips/delete/', id)
    conn = create_connection('cis3368.c2sn9hhzxonj.us-east-1.rds.amazonaws.com', 'ceharp', 'jackson1', 'CIS3368db')

    sql = 'DELETE FROM trips WHERE trip_id = ' + id; 
    execute_query(conn, sql)
    conn.commit()
    return jsonify([])

@app.route('/api/trips/update', methods=['POST'])
def update_trips():
    #update value from trip table
    
    data = request.get_json(silent=True)
    trip_id = data.get("trip_id")
    destination_id = data.get("destination_id")
    transportation = data.get("transportation")
    startdate = data.get("startdate")
    enddate = data.get("enddate")
    tripname = data.get("tripname")
    print('api/trips/update/', trip_id)

    sql = 'UPDATE trips SET destination_id = "' + destination_id + '", transportation = "' + transportation + '", startdate = "' + startdate + '", enddate = "' + enddate + '", tripname = "' + tripname + '" WHERE trip_id = ' + trip_id
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()
    return jsonify(result)


@app.route('/api/trips/create', methods=['POST'])
def create_trips():
    #create trip value
    data = request.get_json(silent=True)
    destination_id = data.get("destination_id")
    transportation = data.get("transportation")
    startdate = data.get("startdate")
    enddate = data.get("enddate")
    tripname = data.get("tripname")
    print("trip create: ", destination_id)

    sql = "INSERT INTO trips (destination_id, transportation, startdate, enddate, tripname) VALUES (%s, %s, %s, %s, %s)"
    val = [(destination_id, transportation, startdate, enddate, tripname)]
    cursor = conn.cursor()
    cursor.executemany(sql, val)
    conn.commit()
    result = cursor.fetchall()
    return jsonify(result)


#api to get all values from the destination table
@app.route('/api/destinations', methods=['GET'])
def get_destinations():
    #selects all values from the destination table
    conn = create_connection('cis3368.c2sn9hhzxonj.us-east-1.rds.amazonaws.com', 'ceharp', 'jackson1', 'CIS3368db')

    sql = 'SELECT * FROM destinations'
    com = execute_read_query(conn, sql)
    return jsonify(com)

@app.route('/api/destinations/<id>', methods=['GET'])
def get_destination(id):
    #selects value from the destination table
    print('api/destinations/', id)
    conn = create_connection('cis3368.c2sn9hhzxonj.us-east-1.rds.amazonaws.com', 'ceharp', 'jackson1', 'CIS3368db')
    sql = 'SELECT * FROM destinations WHERE destination_id = ' + id
    com = execute_read_query(conn, sql)
    return jsonify(com)

@app.route('/api/destinations/delete/<destination_id>', methods=['GET'])
def delete_destinations(destination_id):
    #delete value from destination table
    print('api/destinations/delete/', destination_id)
    conn = create_connection('cis3368.c2sn9hhzxonj.us-east-1.rds.amazonaws.com', 'ceharp', 'jackson1', 'CIS3368db')

    sql = 'DELETE FROM trips WHERE destination_id = ' + destination_id
    execute_query(conn, sql)
    conn.commit()

    sql = 'DELETE FROM destinations WHERE destination_id = ' + destination_id
    execute_query(conn, sql)
    conn.commit()

    return jsonify([])

@app.route('/api/destinations/update', methods=['POST'])
def update_destinations():
    #update value from destination table
    conn = create_connection('cis3368.c2sn9hhzxonj.us-east-1.rds.amazonaws.com', 'ceharp', 'jackson1', 'CIS3368db')
    data = request.get_json(silent=True)
    destination_id = data.get("destination_id")
    country = data.get("country")
    city = data.get("city")
    sightseeing = data.get("sightseeing")
    print("destinations/update: " + destination_id)
    sql = 'UPDATE destinations SET country = "' + country + '", city = "' + city + '", sightseeing = "' + sightseeing + '" WHERE destination_id = ' + destination_id
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/api/destinations/create', methods=['POST'])
def create_destinations():
    #create destination value
    data = request.get_json(silent=True)
    country = data.get("country")
    city = data.get("city")
    sightseeing = data.get("sightseeing")

    sql = "INSERT INTO destinations (country, city, sightseeing) VALUES (%s, %s, %s)"
    val = [(country, city, sightseeing)]
    cursor = conn.cursor()
    cursor.executemany(sql, val)
    conn.commit()
    result = cursor.fetchall()
    return jsonify(result)

app.run()