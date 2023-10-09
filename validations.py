import re

email_re = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
pw_re = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
email = 'email@gmail.com'
pw = 'Senh123!'


def valid_email(email):
    if re.fullmatch(email_re, email):
        print("Valid email")
    else:
        print("Invalid email")


def valid_pw(pw):
    if re.fullmatch(pw_re, pw):
        print("Valid password")
    else:
        print("Invalid password")


def valid_user(user):
    ...


valid_email(email)
valid_pw(pw)