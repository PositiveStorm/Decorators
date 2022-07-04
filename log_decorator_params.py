import logging


def log_decorator(log_path):
    def real_decorator(old_func):

        def new_func(*args):
            result = old_func(*args)
            logging.basicConfig(level=logging.INFO, filename=f'{log_path}', filemode='w',
                                format=f'%(asctime)s - %(message)s - {args} - {result}')
            info = ' Started!'
            logging.info(old_func.__name__ + info)
            return result
        return new_func

    return real_decorator

@log_decorator('123.log')
def summator(x, y):
    z = x + y
    return z

summator(3, 4)