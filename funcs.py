import main


def personal_desc():
    first_name = input("Input your first name: ")
    last_name = input("Input your last name: ")
    age = int(input("Input your age: "))
    email = input("Input your e-mail adress: ")
    password_u = str(input("Create password: "))
    conclude = str(
        input("Do you want to be added to the database? Answer with (yes/no): "))
    if conclude == "yes":
        main.add_user_to_database(
            first_name, last_name, age, email, password_u)
    elif conclude == "no":
        main.want_to_cd()
    else:
        print("Invalid input. Please try again!")
        personal_desc()
    return first_name, last_name, age, email, password_u


def delete_table():
    ask_delete = str(
        input("Do you really want to delete the database? Answer with (yes/no): "))
    if ask_delete == "yes":
        main.c.execute("DROP TABLE pers_info")
        main.conn.commit()
        print("Successfully deleted!")
    elif ask_delete == "no":
        print("Alright! Finished!")
    else:
        print("Invalid input. Please try again!")
        delete_table()
