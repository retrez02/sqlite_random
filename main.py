import sqlite3
import funcs
import request


conn = sqlite3.connect("infotable.db")

c = conn.cursor()


def start():
    what_to_do = input(
        "What to do: Type 'createDatabase':create  database |'deleteDatabase':delete the database | 'add_account':add an account to the database | 'exit':close the program| 'request_info':request stored info about you: ")
    if what_to_do == "createDatabase":
        create_database()
    elif what_to_do == "deleteDatabase":
        funcs.delete_table()
    elif what_to_do == "add_account":
        funcs.personal_desc()
    elif what_to_do == "request_info":
        request.request_info()
    elif what_to_do == "exit":
        return
    else:
        print("Invalid input. Please try again!")
    conn.commit()
    start()


def want_to_cd():
    answer = str(
        input("Are you sure you want to create a database? Answer with (yes/no): "))
    if answer == "yes":
        create_database()
    elif answer == "no":
        start()
    else:
        print("Invalid input. Please try again!")
        want_to_cd()


def add_user_to_database(first_name, last_name, age, email, password_u):
    c.execute(
        "INSERT INTO pers_info VALUES (?,?,?,?,?)", [
            first_name, last_name, age, email, password_u])
    c.execute("SELECT rowid, * FROM pers_info")
    conn.commit()
    items = c.fetchall()

    for item in items:
        print(item)


def create_database():
    c.execute("""CREATE TABLE pers_info (
            first_name text,
            last_name text,
            age int,
            email text,
            password_u text
        )""")


if __name__ == "__main__":

    start()
    print("ccooosfa")
    conn.commit()

    conn.close()
