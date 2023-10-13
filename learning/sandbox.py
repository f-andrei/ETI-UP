import re

email_re = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
pw_re = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
user_re = re.compile(r'^\S{3,40}$')
email = 'emailgmail.com'
pw = 'Senh123'
# user = 'abc'


def valid_email():
    is_valid_e = bool(re.fullmatch(email_re, email))
    return is_valid_e


def valid_pw():
    is_valid_pw = bool(re.fullmatch(pw_re, pw))
    return is_valid_pw


def valid_user():
    is_valid_user = bool(re.fullmatch(user_re, user))
    return is_valid_user

# deve-se criar uma classe para poder utilizar is_valid_user como método.
# while not is_valid_user:
#     user = input("Nome de usuario: ")


while True:
    user = input("User: ")
    valid_user()
    if valid_user():
        break
    else:
        print("Invalid user")

print(valid_pw())
print(valid_email())
print(valid_user())