import time

def chronometre(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'The function "{func.__name__}" is running in chronometre mode')
        result = func(*args, **kwargs)
        end = time.time()
        print(f'The function {func.__name__} execution time is = {end - start:.2f} secs.')
        return result
    return wrapper

def logging(func):
    def wrapper(user, message):
        print(f'Call the function "{func.__name__}" with user : {user} and message : {message}')
        return func(user, message)
    return wrapper

@logging
@chronometre
def send_message(message,user):
    print(f'The message "{message}" is sent to {user}')


send_message(message="Hello word", user="Lilie")