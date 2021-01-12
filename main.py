import sqlite3


conn = sqlite3.connect("infotable.db")

c = conn.cursor()


def start():
    what_to_do = input(
        "What do you want to do: Type 'createDatabase' to create  database | Type 'deleteDatabase' to delete the database | Type 'add_account' to add an account to the database | Type 'exit' to close the program: ")
    if what_to_do == "createDatabase":
        create_database()
    elif what_to_do == "deleteDatabase":
        delete_table()
    elif what_to_do == "add_account":
        personal_desc()
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


def personal_desc():
    first_name = input("Input your first name: ")
    last_name = input("Input your last name: ")
    email = input("Input your e-mail adress: ")
    age = int(input("Input your age: "))
    conclude = str(
        input("Do you want to be added to the database? Answer with (yes/no): "))
    if conclude == "yes":
        add_user_to_database(first_name, last_name, email, age)
    elif conclude == "no":
        want_to_cd()
    else:
        print("Invalid input. Please try again!")
        personal_desc()
    return first_name, last_name, email, age


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


def delete_table():
    ask_delete = str(
        input("Do you really want to delete the database? Answer with (yes/no): "))
    if ask_delete == "yes":
        c.execute("DROP TABLE pers_info")
        conn.commit()
        print("Successfully deleted!")
    elif ask_delete == "no":
        print("Alright! Finished!")
    else:
        print("Invalid input. Please try again!")
        delete_table()


start()

conn.commit()

conn.close()
