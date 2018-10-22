import logging
#testchange

def b():
    return a()

def f():
    return g()

def g():
    return h()

def h():
    logging.debug('About to do h().')
    return i()

def i():
    1/0

def e():
    logging.basicConfig(
        level=logging.DEBUG,
        filename='kaboom1.log',
        filemode='w')

    logging.debug('About to do f().')

    try:
        f()

    except Exception as ex:
        logging.exception(ex)
        raise


if __name__ == '__main__':
    e()