# def decorator(name):
#     print('> decorator:', name)
#     def real_decorator(func):
#         print('>> sam decorator', func.__name__)
#         def decorated(*args, **kwargs):
#             print('>>> pered functi', func.__name__)
#             ret = func(*args, **kwargs)
#             print('>>> posle fuctii', func.__name__)
#             return ret
#         return decorated
#     return real_decorator

# @decorator('test')
# def add(a, b):
#     print('>>>> function add')
#     return a + b

# print('start proggrams')
# r = add(10, 10)
# print(r)
# print('conets programm')

# class DecoratorArgs:
#     def __init__(self, name):
#         print('> Decorator s argumentami __init__:', name)

#     def __call__(self, func):
#         def wrapper(a, b):
#             print('>>> do obernutoi function')
#             func(a, b)
#             print('>>> posle obernutoi functions')
#         return wrapper
    
# @DecoratorArgs("test")
# def add(a, b):
#     print("function add:", a, b)

# print('>> start')
# add(10, 20)
# print('>> conets')

# def decorator(func):
#     '''Decorators'''
#     def decorated():
#         '''Function decorated'''
#         func()
#     return decorated

# @decorator
# def wrapped():
#     '''Obicnaya Function'''
#     print('function wrapped')

# print('start programms')
# print(wrapped.__name__)
# print(wrapped.__doc__)
# print('konets')

# from functools import wraps

# def decorator(func):
#     '''Decorator'''
#     @wraps(func)
#     def decorated():
#         '''function decorated'''
#         func()
#     return decorated

# @decorator
# def wrapped():
#     '''oborachivanie fuction'''
#     print('function wrapped')

# print('start programms')
# print(wrapped.__name__)
# print(wrapped.__doc__)
# print('konets')

# def singleton(cls):
#     '''Class Singleton (1 exampler)'''
#     def wrapper_singleton(*args, **kwargs):
#         if not wrapper_singleton.instance:
#             wrapper_singleton.instance = cls(*args, **kwargs)
#         return wrapper_singleton.instance
#     wrapper_singleton.instance = None
#     return wrapper_singleton

# @singleton
# class TheOne:
#     pass

# print('start')
# first_one = TheOne()
# second_one = TheOne()
# print(id(first_one))
# print(id(second_one))
# print('konets')

user_permissions = ["user"]

def check_permission(permission):
    def wrapper_permission(func):
        def wrapper_check():
            if permission not in user_permissions:
                raise ValueError("Nedostatocno prav")
            return func()
        return wrapper_check
    return wrapper_permission

@check_permission("user")
def check_value():
    return "znachenie"

@check_permission("admin")
def do_something():
    return "tolko admin"

print('start programmi')

check_value()
print('conets')