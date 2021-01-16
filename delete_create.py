import main
from getpass import getpass


def create_database():
    main.c.execute("""CREATE TABLE pers_info (
            first_name text,
            last_name text,
            email text,
            age int,
            key_u int,
            salt int,
            hashed_pw int,
            id_us text
        )""")
    print("Database created!")


def delete_database():
    master_pwd = getpass(
        "Type in the master password to be able to delete the database: ")
    if master_pwd == "123":
        ask_delete = str(
            input("Do you really want to delete the database? Answer with (yes/no): "))
        if ask_delete == "yes":
            main.c.execute("DROP TABLE pers_info")
            main.conn.commit()
            print("Successfully deleted!")
            main.start()
        elif ask_delete == "no":
            print("Alright! Finished!")
            main.start()
        else:
            print("Invalid input. Please try again!")
        delete_database()
    else:
        print("Wrong password. Please try again!")
        delete_database()


def want_to_cd():
    answer = str(
        input("Are you sure you want to create a database? Answer with (yes/no): "))
    if answer == "yes":
        create_database()
    elif answer == "no":
        main.start()
    else:
        print("Invalid input. Please try again!")
        want_to_cd()
