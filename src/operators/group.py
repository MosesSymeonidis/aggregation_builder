def SUM(*expression):
    return {'$sum': list(expression)} if len(expression) > 1 else {'$sum': expression[0]}


def AVG(*expression):
    return {'$avg': list(expression)} if len(expression) > 1 else {'$avg': expression[0]}


def FIRST(expression):
    return {'$first': expression}


def LAST(expression):
    return {'$last': expression}


def MAX(*expression):
    return {'$max': list(expression)} if len(expression) > 1 else {'$max': expression[0]}


def MIN(*expression):
    return {'$min': list(expression)} if len(expression) > 1 else {'$min': expression[0]}


def PUSH(expression):
    return {'$push': expression}


def ADD_TO_SET(expression):
    return {'$addToSet': expression}


def STD_DEV_POP(*expression):
    return {'$stdDevPop': expression} if len(expression) > 1 else {'$stdDevPop': expression[0]}


def STD_DEV_SAMP(*expression):
    return {'$stdDevSamp': list(expression)} if len(expression) > 1 else {'$stdDevSamp': expression[0]}
