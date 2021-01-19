import main
import random
import string
from getpass import getpass
import os
import hashlib
import re


def personal_desc():
    first_name = input("Input your first name: ")
    last_name = input("Input your last name: ")
    email = check_email()
    age = add_age()
    storage, password_u, salt, key_u = create_pwd()
    id_us = id_creation()
    conclude = str(
        input("Do you want to be added to the database? Answer with (yes/no): "))
    if conclude == "yes":
        main.add_user_to_database(
            first_name, last_name, email, age, key_u, salt, storage, id_us, password_u)
    elif conclude == "no":
        print("Alright!")
        return
    else:
        print("Invalid input. Please try again!")
        personal_desc()


def add_age():
    try:
        age = int(input("Enter your age: "))
        while age < 10.0 or age > 150.0:
            age = int(
                input("Your age must be between 10 and 150! Please re-enter your age again: "))
        return age
    except ValueError:
        print("Invalid input! Enter a number")
        return add_age()


def create_pwd():
    password_u = getpass("Enter your password (not shown): ")
    password_r = getpass("Please repeat your password: ")
    if password_u != password_r:
        print("Passwords are not the same! Please repeat")
        create_pwd()
    wrong_symbols = check_password(password_u)
    while len(password_u) < 5 or len(password_u) > 20 or wrong_symbols:
        password_u = str(
            getpass(
                "password must have min 5 chars, can´t contain space ~ * and | it cant be longer than 20 chars! "
                "Please re-enter pwd again: "))
        password_r = str(getpass("Please repeat your password: "))
        wrong_symbols = check_password(password_u)
        if password_r != password_u:
            print("Passwords are not the same! Please repeat")
            create_pwd()
    salt = os.urandom(32)
    key_u = hashlib.pbkdf2_hmac(
        'sha256', password_u.encode('utf-8'), salt, 100000)
    storage = salt + key_u
    return storage, password_u, salt, key_u


def check_password(password_u):
    for letter in password_u:
        if letter in " ~|*":
            return True
    return False


def check_email():
    email = input("Input your e-mail address: ")
    regexp = re.compile(r'@.')
    if regexp.search(email):
        return email
    else:
        print("Must contain @ and .")
        check_email()


def id_creation():
    id_us = "userID#" + "".join(random.choice(string.ascii_letters + string.digits)
                                for _ in range(15))
    main.c.execute("SELECT * FROM pers_info WHERE id_us = ?",
                   (id_us,))
    counter = main.c.fetchall()
    while len(counter) != 0:
        id_us = "userID#" + "".join(random.choice(string.ascii_letters + string.digits)
                                    for _ in range(15))
        main.c.execute("SELECT * FROM pers_info WHERE id_us = ?",
                       (id_us,))
        counter = main.c.fetchall()
    return id_us
