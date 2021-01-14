import main
import funcs


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
        input("Please enter your password: "))

    main.c.execute("SELECT * FROM * WHERE email LIKE ? AND pers_info LIKE ?",
                   ('%'+email_r+'%')('%'+pwd_r+'%'))

    # main.c.execute("SELECT * FROM * WHERE email LIKE ?",
    # ('%'+email_r+'%'))
    # main.c.execute("SELECT * FROM pers_info WHERE password_u LIKE ?",
    # ('%'+pwd_r+'%'))
