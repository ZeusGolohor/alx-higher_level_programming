#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = (a / b)
    except Exception:
        raise
    finally:
        if (result is None):
            print('Inside result: {}'.format(result))
            return (result)
        else:
            print('Inside result: {}'.format(result))
            return (result)
