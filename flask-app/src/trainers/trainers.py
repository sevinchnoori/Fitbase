from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


trainers = Blueprint('trainers', __name__)


# Get all the different trainers from the database
@trainers.route('/members', methods=['GET'])
def get_members():
   # get a cursor object from the database
  
   query = '''
       SELECT first_name, last_name
       FROM Member
   '''
   # use cursor to query the database for a list of products
   cursor = db.get_db().cursor()
   cursor.execute(query)


   # grab the column headers from the returned data
   column_headers = [x[0] for x in cursor.description]


   # create an empty dictionary object to use in
   # putting column headers together with data
   json_data = []


   # fetch all the data from the cursor
   theData = cursor.fetchall()


   # for each of the rows, zip the data elements together with
   # the column headers.
   for row in theData:
       json_data.append(dict(zip(column_headers, row)))


   return jsonify(json_data)


# Get the total number of remaining seats for a class
@trainers.route('/totalseats', methods=['GET'])
def get_seats():
   # get a cursor object from the database
  
   query = '''
       SELECT name, totalSeats
       FROM Class
   '''
   # use cursor to query the database for a list of products
   cursor = db.get_db().cursor()
   cursor.execute(query)


   # grab the column headers from the returned data
   column_headers = [x[0] for x in cursor.description]


   # create an empty dictionary object to use in
   # putting column headers together with data
   json_data = []


   # fetch all the data from the cursor
   theData = cursor.fetchall()


   # for each of the rows, zip the data elements together with
   # the column headers.
   for row in theData:
       json_data.append(dict(zip(column_headers, row)))


   return jsonify(json_data)


# Get all the different members and their contact info from the database
@trainers.route('/contact', methods=['GET'])
def get_contact():
   # get a cursor object from the database
  
   query = '''
       SELECT first_name, last_name, phoneNum_1, email_1
       FROM Member
   '''
   # use cursor to query the database for a list of products
   cursor = db.get_db().cursor()
   cursor.execute(query)


   # grab the column headers from the returned data
   column_headers = [x[0] for x in cursor.description]


   # create an empty dictionary object to use in
   # putting column headers together with data
   json_data = []


   # fetch all the data from the cursor
   theData = cursor.fetchall()


   # for each of the rows, zip the data elements together with
   # the column headers.
   for row in theData:
       json_data.append(dict(zip(column_headers, row)))


   return jsonify(json_data)


# Get all the managers from the database
@trainers.route('/managerinfo', methods=['GET'])
def get_information():
   # get a cursor object from the database
  
   query = '''
       SELECT first, last, email, phoneNum
       FROM Manager
   '''
   # use cursor to query the database for a list of products
   cursor = db.get_db().cursor()
   cursor.execute(query)


   # grab the column headers from the returned data
   column_headers = [x[0] for x in cursor.description]


   # create an empty dictionary object to use in
   # putting column headers together with data
   json_data = []


   # fetch all the data from the cursor
   theData = cursor.fetchall()


   # for each of the rows, zip the data elements together with
   # the column headers.
   for row in theData:
       json_data.append(dict(zip(column_headers, row)))


   return jsonify(json_data)


# Get all the different class information from the database
@trainers.route('/classinfo', methods=['GET'])
def get_classinfo():
   # get a cursor object from the database
  
   query = '''
       SELECT name, startTime, endTime, roomNum
       FROM Class
   '''
   # use cursor to query the database for a list of products
   cursor = db.get_db().cursor()
   cursor.execute(query)


   # grab the column headers from the returned data
   column_headers = [x[0] for x in cursor.description]


   # create an empty dictionary object to use in
   # putting column headers together with data
   json_data = []


   # fetch all the data from the cursor
   theData = cursor.fetchall()


   # for each of the rows, zip the data elements together with
   # the column headers.
   for row in theData:
       json_data.append(dict(zip(column_headers, row)))


   return jsonify(json_data)



# Update the last name of a trainer in the database (in case they get married/change their name!)
@trainers.route('/updateLast', methods=['PUT'])
def update_last():
   the_data = request.json
   current_app.logger.info(the_data)
  
   tid = the_data['tid']
   last = the_data['last']


   query = "UPDATE Trainer SET last = '{}' WHERE tid = {}".format(last, tid)


   current_app.logger.info(query)
   cursor = db.get_db().cursor()
   cursor.execute(query)
   db.get_db().commit()
  
   return 'Last Name Updated!'

#Adds a new trainer to the database (themselves)
@trainers.route('/postTrainer', methods=['POST'])
def new_trainer():
    the_data = request.json
    current_app.logger.info(the_data)
    
    #extracting variable
    first = the_data['first']
    last = the_data['last']
    tid = the_data['tid']
    gender = the_data['gender']

    query = 'INSERT into Trainer (first, last, tid, gender) VALUES ("'
    query += str(first) + '", "'
    query += str(last) + '", "'
    query += str(tid) + '", "'
    query += str(gender) + '")'   
    
    current_app.logger.info(query)
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return 'Trainer created!'

# Deletes a certification of a trainer
@trainers.route('/deleteCertification', methods=['DELETE'])
def delete_certification():
    the_data = request.json
    current_app.logger.info(the_data)
    
    tid = the_data['tid']
    query = 'DELETE FROM Certs WHERE tid = '  + str(tid)
    
    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return 'Trainer certification deleted!'