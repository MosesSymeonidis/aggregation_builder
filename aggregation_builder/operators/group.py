def SUM(*expression):
    """
    Calculates and returns the sum of numeric values.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/sum/
    for more details
    :param expression: expression or variables
    :return: Aggregation operator
    """
    return {'$sum': list(expression)} if len(expression) > 1 else {'$sum': expression[0]}


def AVG(*expression):
    """
    Calculates and returns the average of numeric values.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/avg/
    for more details
    :param expression: expression or variables
    :return: Aggregation operator
    """
    return {'$avg': list(expression)} if len(expression) > 1 else {'$avg': expression[0]}


def FIRST(expression):
    """
    Returns the value that results from applying an expression to the first document in a group of documents that share the same group by key.
    Only meaningful when documents are in a defined order.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/first/
    for more details
    :param expression: expression or variables
    :return: Aggregation operator
    """
    return {'$first': expression}


def LAST(expression):
    """
    Returns the value that results from applying an expression to the last document in a group of documents that share the same group by key.
    Only meaningful when documents are in a defined order.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/last/
    for more details
    :param expression: expression or variables
    :return: Aggregation operator
    """
    return {'$last': expression}


def MAX(*expression):
    """
    Returns the maximum value.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/max/
    for more details
    :param expression: expression/expressions or variables
    :return: Aggregation operator
    """
    return {'$max': list(expression)} if len(expression) > 1 else {'$max': expression[0]}


def MIN(*expression):
    """
    Returns the minimum value.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/min/
    for more details
    :param expression: expression/expressions or variables
    :return: Aggregation operator
    """
    return {'$min': list(expression)} if len(expression) > 1 else {'$min': expression[0]}


def PUSH(expression):
    """
    Returns an array of all values that result from applying an expression
    to each document in a group of documents that share the same group by key.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/push/
    for more details
    :param expression: expression
    :return: Aggregation operator
    """
    return {'$push': expression}


def ADD_TO_SET(expression):
    """
    Returns an array of all unique values that results from applying an expression
    to each document in a group of documents that share the same group by key.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/addToSet/
    for more details
    :param expression: expression
    :return: Aggregation operator
    """
    return {'$addToSet': expression}


def STD_DEV_POP(*expression):
    """
    Calculates the population standard deviation of the input values.
    Use if the values encompass the entire population of data you want to represent
    and do not wish to generalize about a larger population.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/stdDevPop/
    for more details
    :param expression: expression/expressions
    :return: Aggregation operator
    """
    return {'$stdDevPop': expression} if len(expression) > 1 else {'$stdDevPop': expression[0]}


def STD_DEV_SAMP(*expression):
    """
    Calculates the sample standard deviation of the input values.
    Use if the values encompass a sample of a population of data from which to generalize about the population.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/stdDevSamp/
    for more details
    :param expression: expression/expressions
    :return: Aggregation operator
    """
    return {'$stdDevSamp': list(expression)} if len(expression) > 1 else {'$stdDevSamp': expression[0]}
