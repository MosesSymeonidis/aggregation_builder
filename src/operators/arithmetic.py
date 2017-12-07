def ABS(expression):
    return {'$abs': expression}


def ADD(*expressions):
    return {'$add': list(expressions)}


def CEIL(expression):
    return {'$ceil': expression}


def DIVIDE(x, y):
    return {'$divide': [x, y]}


def EXP(number):
    return {'$exp': number}


def FLOOR(number):
    return {'$floor': number}


def LN(number):
    return {'$ln': number}


def LOG(number, base):
    return {'$log': [number, base]}


def LOG10(number):
    return {'$log10': number}


def MOD(x, y):
    return {'$mod': [x, y]}


def MULTIPLY(*expressions):
    return {'$multiply': list(expressions)}


def POW(number, exponent):
    return {'$pow': [number, exponent]}


def SQRT(number):
    return {'$sqrt': number}


def SUBTRACT(x, y):
    return {'$subtract': [x, y]}


def TRUNC(number):
    return {'$trunc': number}
