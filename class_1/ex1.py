"""
def add(x, y):
    return x + y

my_sum = add
result = add(2, 3)
num = 1
print(num())
"""

def add(x, y):
    return x + y

add = lambda x, y: x + y

add(2, 3)
# Validation: (username, password) > True | False
# 1. username doesn't exist
# 2. password longer than 6 chars
# 3. password contains at least 1 symbol

def check_username_doesnt_exist(username, password):
    pass


def check_password_longer_than_six_chars(username, password):
    pass

VALIDATORS = [
    check_username_doesnt_exist,
    check_password_longer_than_six_chars,
    check_password_contains_symbol
]

def create_user(username, password):
    for validator in VALIDATORS:
        if not validator(username, password):
            raise ValueError("Doesn't validate")

    insert_in_databse(
        'user', {'username': username
        'password': password})


def create_user(username, password, method='db'):
    create_user_actual_function = insert_in_databse
    if method == 'log':
        create_user_actual_function = log_user_instead_of_saving_it

    create_user_actual_function(
        'user', {'username': username
        'password': password})



"""
def create_user(username, password):
    if not check_username_doesnt_exist(username, password):
        raise ValueError("Doesn't validate")
    if not check_password_longer_than_six_chars(username, password):
        raise ValueError("Doesn't validate")

    insert_in_databse(
        'user', {'username': username
        'password': password})
"""