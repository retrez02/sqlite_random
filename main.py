import sqlite3


conn = sqlite3.connect("infotable.db")

c = conn.cursor()


def want_to_cd():
    answer = str(
        input("Do you want to create a database? Answer with (yes/no)!"))
    if answer == "yes":
        create_database()
    elif answer == "no":
        personal_desc()
    else:
        print("Invalid input. Please try again!")
        want_to_cd()


def personal_desc():
    first_name = str(input("Input your first name: ")),
    last_name = str(input("Input your last name: ")),
    email = str(input("Input your e-mail adress: ")),
    age = str(input("Input your age: ")),


def create_database():
    c.execute("""CREATE TABLE pers_info (
            first_name text,
            last_name text,
            email text,
            age int
        )""")


want_to_cd()

conn.commit()

conn.close()
