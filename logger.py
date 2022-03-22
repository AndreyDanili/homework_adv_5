from datetime import datetime

def write(data, path_file):
    with open(path_file, 'w') as file:
        file.write(f'{data}\n')


def logger_simple(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        write(f'Время вызова функции: {datetime.now()}\n'
              f'Имя функции: {old_function.__name__}\n'
              f'Аргументы функции: {args, kwargs}\n'
              f'Возвращаемое значение функци: {result}', 'log_file_simple.txt')
        return result

    return new_function


def parametrized_logger(parameter):
    def logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            write(f'Время вызова функции: {datetime.now()}\n'
                  f'Имя функции: {old_function.__name__}\n'
                  f'Аргументы функции: {args, kwargs}\n'
                  f'Возвращаемое значение функци: {result}', parameter)
            return result

        return new_function

    return logger


@logger_simple
def function_simple(a, b):
    return a * b


@parametrized_logger('log_file.txt')
def function(a, b):
    return a * b


res_simple = function_simple(5, 3)
res = function(7, 3)