import sqlite3
import funcs


conn = sqlite3.connect("infotable.db")

c = conn.cursor()


def start():
    what_to_do = input(
        "What do you want to do: Type 'createDatabase' to create  database | Type 'deleteDatabase' to delete the database | Type 'add_account' to add an account to the database | Type 'exit' to close the program: ")
    if what_to_do == "createDatabase":
        create_database()
    elif what_to_do == "deleteDatabase":
        funcs.delete_table()
    elif what_to_do == "add_account":
        funcs.personal_desc()
    elif what_to_do == "exit":
        exit()
    else:
        print("Invalid input. Please try again!")
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


def add_user_to_database(first_name, last_name, email, age):
    c.execute(
        "INSERT INTO pers_info VALUES (?,?,?,?)", [
            first_name, last_name, email, age])
    c.execute("SELECT rowid, * FROM pers_info")
    items = c.fetchall()

    for item in items:
        print(item)


def create_database():
    c.execute("""CREATE TABLE pers_info (
            first_name text,
            last_name text,
            email text,
            age int
        )""")

if __name__ == "__main__":
    start()

    conn.commit()

    conn.close()
