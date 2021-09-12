from flask import g
import sqlite3


DATABASE = "user.db"


def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def output_formatter(results: tuple):
    out = []
    for result in results:
        result_dict = {}
        result_dict["id"] = result[0]
        result_dict["first_name"] = result[1]
        result_dict["last_name"] = result[2]
        result_dict["hobbies"] = result[3]
        result_dict["active"] = result[4]
        out.append(result_dict)
    return out


def scan():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def read(pk): # personal key
    cursor = get_db().execute(
        "SELECT * FROM user WHERE id=?", (pk, ))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def insert(fn,ln,h): # first name, last name, hobbies
    cursor = get_db()
    last_row_id = cursor.execute(
        "INSERT INTO user (first_name, last_name, hobbies) VALUES (?, ?, ?)", (fn, ln, h) ).lastrowid
    cursor.commit()
    cursor.close
    return last_row_id

def update(pk,fn,ln,h): # personal key, first name, last name, hobbies
    cursor = get_db().execute(
        "UPDATE user SET first_name=?, last_name=?, hobbies=? WHERE id=? ", (fn, ln, h, pk)
        )
    cursor.commit()
    cursor.close
    return output_formatter(cursor)
    
def delete(pk):
    cursor = get_db().execute(
        "UPDATE user SET active=0 WHERE id=?", (pk)
        )
    cursor.commit()
    cursor.close
    return output_formatter(cursor)