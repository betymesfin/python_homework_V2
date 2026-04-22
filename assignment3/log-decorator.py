import logging


logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        if args :
           pos_args = args
        else: 
            pos_args="none"
        if kwargs:
            kw_args = kwargs
        else: 
            kw_args="none"
        result = func(*args, **kwargs)
        logger.info(f"function: {func_name}")
        logger.info(f"positional parameters: {pos_args}")
        logger.info(f"keyword parameters: {kw_args}")
        logger.info(f"return: {result}")
        return result
    return wrapper

@logger_decorator
def greet():
    print("Hello, World!")

@logger_decorator
def check_values(*args):
    print("args:", args)
    # return True

@logger_decorator
def return_decorator(**kwargs):
    print("Keyword arguments received:", kwargs)
    return logger_decorator

greet()
check_values(10, 20, 30)
return_decorator(name="beth", age="?")