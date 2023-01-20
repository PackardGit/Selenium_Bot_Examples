def logger(f):
    """results: Decorator that generate json file to associated tests
    :param f: Function that uses this decorator
    """
    def logger_wrapper(*args, **kwargs):
        return_element = False
        try:
            args = f(*args, **kwargs)
            log_info = args[0]
            return_element = args[1]
            print(log_info)
        except IndexError as e:
            print(e)
            print("Calling function does not provide required parameters")
            return_element = False
        except Exception as e:
            print(e)
            return_element = False
        finally:
            return return_element
    return logger_wrapper
