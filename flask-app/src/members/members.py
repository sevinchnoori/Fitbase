from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

members = Blueprint('members', __name__)

# Adds a new member into the database (themselves)
@members.route('/postMember', methods=['POST'])
def new_member():
    the_data = request.json
    current_app.logger.info(the_data)
    
    #extracting variable
    mid = the_data['mid']
    first_name = the_data['first_name']
    last_name = the_data['last_name']
    gender = the_data['gender']
    years = the_data['years']
    age = the_data['age']
    phoneNum_1 = the_data['phoneNum_1']
    phoneNum_2 = the_data['phoneNum_2']
    email_1 = the_data['email_1']
    email_2 = the_data['email_2']

    query = 'INSERT into Member (mid, first_name, last_name, gender, years, age,\
        phoneNum_1, phoneNum_2, email_1,email_2) VALUES ("'
    query += str(mid) + '", "'
    query += str(first_name) + '", "'
    query += str(last_name) + '", "'
    query += str(gender) + '", "'
    query += str(years) + '", "'
    query += str(age) + '", "'
    query += str(phoneNum_1) + '", "'
    query += str(phoneNum_2) + '", "'
    query += str(email_1) + '", "'
    query += str(email_2) + '")'   
    
    current_app.logger.info(query)
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return 'Member created!'


# Get all the orders made
@members.route('/orders', methods=['GET'])
def get_orders():
    # get a cursor object from the database
    
    query = '''
        SELECT oid, totalCost, mid
        FROM Orders
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


# Get all the classes and their times from the database
@members.route('/classNames', methods=['GET'])
def get_classes():
    # get a cursor object from the database
    
    query = '''
        SELECT name, startTime, endTime
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


# Update the membership
@members.route('/updateType', methods=['PUT'])
def update_type():
    the_data = request.json
    current_app.logger.info(the_data)
    
    mid = the_data['mid']
    msid = the_data['msid']

    query = "UPDATE Member SET msid = '{}' WHERE mid = {}".format(msid, mid)

    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Membership Updated!'

# Get the costs of all the memberships available
@members.route('/membershipPrices', methods=['GET'])
def get_membership_prices():
    # get a cursor object from the database
    
    query = '''
        SELECT type, price
        FROM Membership
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


# Get the names of the trainers 
@members.route('/trainerNames', methods=['GET'])
def get_trainers():
    # get a cursor object from the database
    
    query = '''
        SELECT first, last
        FROM Trainer
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

# Get information about personal training sessions
@members.route('/getPT', methods=['GET'])
def get_personal_training():
    # get a cursor object from the database
    
    query = '''
        SELECT ptid, activity, length
        FROM PersonalTraining
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


# Deletes own member account
@members.route('/deleteAccount', methods=['DELETE'])
def delete_account():
    the_data = request.json
    current_app.logger.info(the_data)
    
    mid = the_data['mid']
    query = 'DELETE FROM Member WHERE mid = '  + str(mid)
    
    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return 'Member account deleted!'




