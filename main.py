import sqlite3
import user
import request
import delete_create


conn = sqlite3.connect("infotable.db")

c = conn.cursor()


def start():
    what_to_do = input(
        "Type 'create_database': create database | 'delete_database': delete database | 'add_acc': add account | "
        "'exit': close | 'request_info': request stored info about you: ")
    if what_to_do == "create_database":
        delete_create.create_database()
    elif what_to_do == "delete_database":
        delete_create.delete_database()
    elif what_to_do == "add_acc":
        user.personal_desc()
    elif what_to_do == "request_info":
        request.request_info()
    elif what_to_do == "exit":
        return
    else:
        print("Invalid input. Please try again!")
    conn.commit()
    start()


def add_user_to_database(first_name, last_name, email, age, key_u, salt, storage, id_us, password_u):
    c.execute(
        "INSERT INTO pers_info VALUES (?,?,?,?,?,?,?,?)", [
            first_name, last_name, email, age, key_u, salt, storage, id_us])
    c.execute("SELECT rowid, * FROM pers_info")
    conn.commit()
    c.execute("SELECT * FROM pers_info ORDER BY rowid DESC LIMIT 1")
    items = c.fetchall()
    for item in items:
        print(str(item[0]) + "\t" + str(item[1]) + "\t" +
              str(item[2]) + "\t" + str(item[3]) + "\t" + password_u)


if __name__ == "__main__":

    start()
    print("#exit")
    conn.commit()
    conn.close()
