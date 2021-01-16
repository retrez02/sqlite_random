import main
import funcs
import os
import hashlib
from getpass import getpass
# from pprint import pprint


def request_info():
    user_request = str(
        input("Do you want to see all data we store about you? Answer with (yes/no): "))
    if user_request == "yes":
        request_handler()
    elif user_request == "no":
        main.start()
    else:
        print("Invalid input. Please try again!")
        request_info()


def request_handler():
    main.c.execute("SELECT * FROM pers_info ORDER BY rowid DESC LIMIT 1")

    salt = b''

    key = b''

    email_r = str(
        input("Please enter your e-mail adress: "))
    pwd_r = str(
        getpass("Please enter your password: "))

    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        pwd_r.encode('utf-8'),
        salt,
        100000
    )

    if new_key == key:
        print('Password is correct')
    else:
        print('Password is incorrect')
        request_handler()

    main.c.execute("SELECT * FROM pers_info WHERE email == ? AND storage == ?",
                   ((email_r), (new_key),))
    users = main.c.fetchall()
    if len(users) == 0:
        print("Not the correct data! Please try again!")
        request_handler()
    for user in users:
        print(str(user[0]) + "\t" + str(user[1]) + "\t" +
              str(user[2]) + "\t" + str(user[3]) + "\t" + pwd_r)
