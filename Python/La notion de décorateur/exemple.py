### Exemple 1
# def decorate(func):			# Definition du décorateur
#     def wrapper(*args):		# Définition de la function wrapper
#         y = func(*args)
#         result = y*100
#         print(result)
#         return result
#     return wrapper			# Le décorateur renvoie le wrapper
#
#
# @decorate				# Spécification du décorateur: y = func(*args) soit ici : y = divide(a, b)
# def divide(a, b):
#     return a/b
#
#
# divide(10,100)

### Exemple 2
# def decorate_with_params(message_before, message_after):
#     def decorate(func):
#         def wrapper():
#             print(message_before)
#             func()                  # represente la fonction hello()
#             print(message_after)
#         return wrapper
#     return decorate
#
# @decorate_with_params("Before", "After")
# def hello():
#     print("Hello!")
#
# hello()


### Exemple 3

def decorate_outer(func):
    def wrapper():
        print("begin outer decorate")
        func()
        print("end outer decorate")
    return wrapper

def decorate_inner(func):
    def wrapper():
        print("begin inner decorate")
        func()
        print("end inner decorate")
    return wrapper

@decorate_outer
@decorate_inner
def my_fun():
    print("Initial function")

my_fun()