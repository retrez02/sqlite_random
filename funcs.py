import main
import random
import string
from getpass import getpass


def check_password(password_u):
    for letter in password_u:
        if letter in " ~|*":
            return True
    return False


def create_pwd():
    password_u = getpass("Enter your password (not shown): ")
    password_r = getpass("Please repeat your password: ")
    if password_u != password_r:
        print("Passwords are not the same! Please repeat")
        create_pwd()
    wrong_symbols = check_password(password_u)
    while len(password_u) < 5 or len(password_u) > 20 or wrong_symbols == True:
        password_u = str(
            getpass("password must have min 5 chars, can´t contain space ~ * and | it cant be longer than 20 chars! Please re-enter pwd again: "))
        password_r = str(getpass("Please repeat your password: "))
        wrong_symbols = check_password(password_u)
        if password_r != password_u:
            print("Passwords are not the same! Please repeat")
            create_pwd()
    return password_u


def personal_desc():
    first_name = input("Input your first name: ")
    last_name = input("Input your last name: ")
    age = int(input("Input your age: "))

    email = input("Input your e-mail adress: ")
    password_u = create_pwd()
    # wrong_email = check_email(email)
    # while wrong_email == True:
    #     email = str(
    #         input("E-Mail adress must contain @ and . | Please enter again: "))
    #     wrong_email = check_email(email)
    id_us = "userID#" + "".join(random.choice(string.ascii_letters + string.digits)
                                for _ in range(15))
    conclude = str(
        input("Do you want to be added to the database? Answer with (yes/no): "))
    if conclude == "yes":
        main.add_user_to_database(
            first_name, last_name, age, email, password_u, id_us)
    elif conclude == "no":
        return
    else:
        print("Invalid input. Please try again!")
        personal_desc()

    return first_name, last_name, age, email, password_u, id_us


def check_email(email):
    return
    # for letter in email:
    #     if letter in ".@":
    #         return False
    # return True


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
