def AND(*expressions):
    """
    Evaluates one or more expressions and returns true if all of the expressions are true.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/and/
    for more details
    :param expressions: An array of expressions
    :return: Aggregation operator
    """
    return {'$and': list(expressions)}


def OR(*expressions):
    """
    Evaluates one or more expressions and returns true if any of the expressions are true.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/or/
    for more details
    :param expressions: An array of expressions
    :return: Aggregation operator
    """
    return {'$or': list(expressions)}


def NOT(expression):
    """
    Evaluates a boolean and returns the opposite boolean value.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/not/
    for more details
    :param expression: An array of expressions
    :return: Aggregation operator
    """
    return {'$not': [expression]}
