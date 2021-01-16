import main
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

    email_r = str(
        input("Please enter your e-mail adress: "))
    pwd_r = str(
        getpass("Please enter your password: "))

    main.c.execute("SELECT * FROM pers_info WHERE email = ?",
                   (email_r,))
    get_info = main.c.fetchall()
    if len(get_info) == 0:
        print("Not the correct data! Please try again!")
        request_handler()
    if len(get_info[0]) == 0:
        print("Not the correct data! Please try again!")
        request_handler()

    salt = bytes(get_info[0][5])
    key_u = bytes(get_info[0][4])

    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        pwd_r.encode('utf-8'),
        salt,
        100000
    )

    if new_key == key_u:
        print('Password is correct')
    else:
        print('Password is incorrect')
        request_handler()

    main.c.execute("SELECT * FROM pers_info WHERE email == ? AND key_u == ?",
                   ((email_r), (new_key)))
    users = main.c.fetchall()
    if len(users) == 0:
        print("Not the correct data! Please try again!")
        request_handler()
    for user in users:
        print(str(user[0]) + "\t" + str(user[1]) + "\t" +
              str(user[2]) + "\t" + str(user[3]) + "\t" + str(pwd_r))
