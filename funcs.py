import main
from getpass import getpass


def personal_desc():
    first_name = input("Input your first name: ")
    last_name = input("Input your last name: ")
    age = int(input("Input your age: "))

    email = input("Input your e-mail adress: ")

    # wrong_email = check_email(email)
    # while wrong_email == True:
    #     email = str(
    #         input("E-Mail adress must contain @ and . | Please enter again: "))
    #     wrong_email = check_email(email)

    password_u = getpass("Enter your password: ")
    wrong_symbols = check_password(password_u)
    while len(password_u) < 5 or len(password_u) > 20 or wrong_symbols:
        password_u = str(
            input("password must have min 5 chars, can´t contain space ~ * and | it cant be longer than 20 chars! Please re-enter pwd again: "))
        wrong_symbols = check_password(password_u)
    conclude = str(
        input("Do you want to be added to the database? Answer with (yes/no): "))
    if conclude == "yes":
        main.add_user_to_database(
            first_name, last_name, age, email, password_u)
    elif conclude == "no":
        return
    else:
        print("Invalid input. Please try again!")
        personal_desc()
    return first_name, last_name, age, email, password_u


def check_email(email):
    return
    # for letter in email:
    #     if letter in ".@":
    #         return False
    # return True


def check_password(password_u):
    for letter in password_u:
        if letter in " ~|*":
            return True
    return False


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
