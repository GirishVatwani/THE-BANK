import mysql.connector as dbconnector
#import pandas as pd

def is_safe(lst):
    for i in lst:
        if any(c in i.lower() for c in ["=", " or ", "!", "//", "'", '"', ";", "(", ")", "and", '"']):
            return False
    return True

def insert_data(cursor, data, table):
    if is_safe(data.values()):
        columns = ", ".join(f"{column}" for column in data.keys())
        values = ",".join(f"'{value}'" for value in data.values())
        query = "INSERT INTO %s %s VALUES %s"
        cursor.execute(query, (table, tuple(columns), tuple(values)))
        return "Sucessfull"
    else:
        return "SQLInjectionFound"
        
def delete_row(cursor, table, which_id, id):
    if is_safe([id]):
        query = "DELETE FROM %s WHERE %s = %s"
        cursor.execute(query, (table, which_id, id))
        return "Sucessfull"
    else:
        return "SQLInjectionFound"

def update_field(cursor, table, key, value, which_id, id):
        if is_safe([id, key, value, table]):
            query = "UPDATE %s SET %s = %s WHERE %s = %s"
            cursor.execute(query, (table, key, value, which_id, id))
            return "Sucessfull"
        else:
            return "SQLInjectionFound"
        
def get_data(table):
    
     return

def existing_user(cursor, message_id, username = None):
    cursor.execute("SELECT * FROM coustomers WHERE messanger_id = %s", (message_id,))
    if cursor.fetchone():
        return True
    else:
        return False

if __name__ == "__main__":
    mydb = dbconnector.connect(host="<your_host/localhost>", user="<database_username>", passwd="<acess- password>", database = "<database__name>")
    if mydb.is_connected():
        mycursor = mydb.cursor()
        if query == "SafityIssue502":
            print("⚠️SQL Injection Detected⚠️")
        else:
            mycursor.execute(query)
            mydb.commit()
            print("Query Commited Sucellfully")

        mycursor.execute("SELECT * FROM voter WHERE VoterID = %s", ('PRS9090',)) Method to Bypass injection
        print(mycursor.fetchone()) Will give first row
        data = get_data()
        query = get_insert_query(data, "voter")
        print(query)
        if existing_user(mycursor, get_delete()):
            print("User already exists")
        else:
            print("User does not exist")

        mycursor.execute(query, placeholders)


    else:
        print("Connection failed!")


