from enum import Enum, auto
import sqlite3
from sqlite3 import Error
import string
import sys
import os
import src.utility.path as util_path


DB_FILENAME = 'sqlite_db.db'
SQL_SCRIPT_FILENAME = 'sql_script.db'
DB_PATH = util_path.get_correct_path_of_db(DB_FILENAME)
SQL_PATH = util_path.get_correct_path_of_db(SQL_SCRIPT_FILENAME)

def create_db_if_can():
    con = create_connection()
    cursor = con.cursor()
        
    with open(SQL_PATH, "r") as script_f:
        sql_script = script_f.read()
    
    cursor.executescript(sql_script)
    con.commit()
    con.close()
    
# Creats a connection to the database
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(DB_PATH)
        print("Connected to database!")
    except Error as e:
        print(f"Error: {e}")
        
    return connection

# SQL query to ADD data
# Requires a TABLE to work on and VALUES to add
def sql_add_query(table, columns, values) -> bool:    
    
    # Create connection
    connection = create_connection()
    cur = connection.cursor()
    
    to_return = False
    # Check if LIST(Columns) and Table exists 
    try:
        cur.execute(f"INSERT INTO {table} {columns} VALUES {place_holder_counter(len(values))}", values)
        print("Insertion complete")
        to_return = True
        connection.commit()
    except Exception as e:
        to_return = False
        print(f"Error: {e}")

    return to_return

# SQL query to DELETE data
# Requires a TABLE to work on and VALUES to delete
def sql_delete_query(table, id) -> bool:
    # Create connection
    connection = create_connection()
    cur = connection.cursor()
    
    to_return = False
    try:
        cur.execute(f"DELETE FROM {table} WHERE ID = ?", str(id))
        to_return = True
        print("Delete complete")
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")

    return to_return

# SQL query to DELETE ALL data
# Requires a TABLE to work on and VALUES to delete
def sql_delete_all_query(table) -> bool:
    # Create connection
    connection = create_connection()
    cur = connection.cursor()
    
    to_return = False
    try:
        cur.execute(f"DELETE FROM {table}")
        to_return = True
        print("Delete complete")
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")

    return to_return

# SQL query to UPDATE data
# Requires a TABLE to work on and VALUES to edit
def sql_update_query_of_id(table, column, values) -> bool:
    # Create connection
    connection = create_connection()
    cur = connection.cursor()
    
    to_return = False
    try:
        cur.execute(f"UPDATE {table} SET {column} = ? WHERE ID = ?", values)
        to_return = True
        print("Update complete")
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")

    return to_return

# SQL query to SELECT data
# Requires a TABLE to work on and ID to select
def sql_select_by_id_query(table, id) -> list:
    # Create connection
    connection = create_connection()
    cur = connection.cursor()
    results = []
    
    try:
        cur.execute(f"SELECT * FROM {table} WHERE ID = ?", (str(id),))
        results = cur.fetchall()
        
    except Exception as e:
        print(f"Error: {e}")

    return results
    
# SQL query to SELECT ALL data
# Requires a TABLE to work on
def sql_select_all_query(table) -> list:
    # Create connection
    connection = create_connection()
    cur = connection.cursor()
    results = []
    
    try:
        cur.execute(f"SELECT * FROM {table}")
        results = cur.fetchall()
        
    except Exception as e:
        print(f"Error: {e}")

    return results
    
# Returns string of placeholders for SQL query
def place_holder_counter(length_of_values) -> string:
    placeholders = "("
    for i in range(0, length_of_values):
        if i == length_of_values-1:
            placeholders += "?)"
        else:    
            placeholders += "?, "
    return placeholders

def get_columns_of_table(table) -> list:
    # Create connection
    connection = create_connection()
    cur = connection.cursor()

    try:
        cur.execute(f"PRAGMA table_info({table.lower()});")
        result_columns = cur.fetchall()
    except Exception as e:
        print(f"Error: {e}")
    
    # Filtering data for names
    result_col_names = []
    for i in result_columns:
        result_col_names.append(i[1])
    
    return result_col_names


create_db_if_can()