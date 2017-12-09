def CMP(x=None, y=None):
    """
    Compares two values and returns:
        -1 if the first value is less than the second.
        1 if the first value is greater than the second.
        0 if the two values are equivalent.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/cmp/
    for more details
    :param x: first value or expression
    :param y: second value or expression
    :return: Aggregation operator
    """
    if x is None and y is None:
        return {'$cmp': []}
    return {'$cmp': [x, y]}


def EQ(x=None, y=None):
    """
    Compares two values and returns:
        true when the values are equivalent.
        false when the values are not equivalent.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/eq/
    for more details
    :param x: first value or expression
    :param y: second value or expression
    :return: Aggregation operator
    """
    if x is None and y is None:
        return {'$eq': []}
    return {'$eq': [x, y]}


def GT(x=None, y=None):
    """
    Compares two values and returns:
        true when the first value is greater than the second value.
        false when the first value is less than or equivalent to the second value.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/gt/
    for more details
    :param x: first value or expression
    :param y: second value or expression
    :return: Aggregation operator
    """
    if x is None and y is None:
        return {'$gt': []}
    return {'$gt': [x, y]}


def GTE(x=None, y=None):
    """
    Compares two values and returns:
        true when the first value is greater than or equivalent to the second value.
        false when the first value is less than the second value.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/gte/
    for more details
    :param x: first value or expression
    :param y: second value or expression
    :return: Aggregation operator
    """
    if x is None and y is None:
        return {'$gte': []}
    return {'$gte': [x, y]}


def LT(x=None, y=None):
    """
    Compares two values and returns:
        true when the first value is less than the second value.
        false when the first value is greater than or equivalent to the second value.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/lt/
    for more details
    :param x: first value or expression
    :param y: second value or expression
    :return: Aggregation operator
    """
    if x is None and y is None:
        return {'$lt': []}
    return {'$lt': [x, y]}


def LTE(x=None, y=None):
    """
    Compares two values and returns:
        true when the first value is less than or equivalent to the second value.
        false when the first value is greater than the second value.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/lte/
    for more details
    :param x: first value or expression
    :param y: second value or expression
    :return: Aggregation operator
    """
    if x is None and y is None:
        return {'$lte': []}
    return {'$lte': [x, y]}


def NE(x=None, y=None):
    """
    Compares two values and returns:
        true when the values are not equivalent.
        false when the values are equivalent.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/ne/
    for more details
    :param x: first value or expression
    :param y: second value or expression
    :return: Aggregation operator
    """
    if x is None and y is None:
        return {'$ne': []}
    return {'$ne': [x, y]}
