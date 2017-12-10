def ABS(expression):
    """
    Returns the absolute value of a number.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/abs/
    for more details
    :param expression: The number or field of number
    :return: Aggregation operator
    """
    return {'$abs': expression}


def ADD(*expressions):
    """
    Adds numbers together or adds numbers and a date.
    If one of the arguments is a date, $add treats the other arguments as milliseconds to add to the date.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/add/
    for more details
    :param expressions: The numbers or fields of number
    :return: Aggregation operator
    """
    return {'$add': list(expressions)}


def CEIL(expression):
    """
    Returns the smallest integer greater than or equal to the specified number.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/ceil/
    for more details
    :param expression: The number or field of number
    :return: Aggregation operator
    """
    return {'$ceil': expression}


def DIVIDE(x, y):
    """
    Divides one number by another and returns the result.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/divide/
    for more details
    :param x: The number or field of number (is the dividend)
    :param y: The number or field of number (is the divisor)
    :return: Aggregation operator
    """
    return {'$divide': [x, y]}


def EXP(number):
    """
    Returns the exponential value of a number.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/exp/
    for more details
    :param number: The number or field of number
    :return: Aggregation operator
    """
    return {'$exp': number}


def FLOOR(number):
    """
    Returns the largest integer less than or equal to the specified number.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/floor/
    for more details
    :param number: The number or field of number
    :return: Aggregation operator
    """
    return {'$floor': number}


def LN(number):
    """
    Calculates the natural logarithm ln of a number and returns the result as a double.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/ln/
    for more details
    :param number: The number or field of number
    :return: Aggregation operator
    """
    return {'$ln': number}


def LOG(number, base):
    """
    Calculates the log of a number in the specified base and returns the result as a double.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/log/
    for more details
    :param number: The number or field of number
    :param base: The base of log operation
    :return: Aggregation operator
    """
    return {'$log': [number, base]}


def LOG10(number):
    """
    Calculates the log base 10 of a number and returns the result as a double.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/log10/
    for more details
    :param number: The number or field of number
    :return: Aggregation operator
    """
    return {'$log10': number}


def MOD(x, y):
    """
    Divides one number by another and returns the remainder.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/mod/
    for more details
    :param x: The number or field is the dividend,
    :param y: The number or field is the divisor,
    :return: Aggregation operator
    """
    return {'$mod': [x, y]}


def MULTIPLY(*expressions):
    """
    Multiplies numbers together and returns the result.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/multiply/
    for more details
    :param expressions: An array of numbers or fields
    :return: Aggregation operator
    """
    return {'$multiply': list(expressions)}


def POW(number, exponent):
    """
    Raises a number to the specified exponent and returns the result.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/pow/
    for more details
    :param number: The number or field that will be raised
    :param exponent: The number or field that will be the exponent
    :return: Aggregation operator
    """
    return {'$pow': [number, exponent]}


def SQRT(number):
    """
    Calculates the square root of a positive number and returns the result as a double.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/sqrt/
    for more details
    :param number: The number or field of number
    :return: Aggregation operator
    """
    return {'$sqrt': number}


def SUBTRACT(x, y):
    """
    Subtracts two numbers to return the difference,
    or two dates to return the difference in milliseconds,
    or a date and a number in milliseconds to return the resulting date.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/subtract/
    for more details
    :param x: The number or field of number
    :param y: The number or field of number (is subtracted from the first argument)
    :return: Aggregation operator
    """
    return {'$subtract': [x, y]}


def TRUNC(number):
    """
    Truncates a number to its integer.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/trunc/
    for more details
    :param number: The number or field of number
    :return: Aggregation operator
    """
    return {'$trunc': number}
