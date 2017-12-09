def SET_EQUALS(*expressions):
    """
    Compares two or more arrays and returns true if they have the same distinct elements and false otherwise.
    https://docs.mongodb.com/manual/reference/operator/aggregation/setEquals/
    for more details
    :param expressions: The arrays (expressions) which will be compared
    :return: Aggregation operator
    """
    return {'$setEquals': list(expressions)}


def SET_INTERSECTION(*expressions):
    """
    Takes two or more arrays and returns an array that contains the elements that appear in every input array.
    https://docs.mongodb.com/manual/reference/operator/aggregation/setIntersection/
    for more details
    :param expressions: The arrays (expressions)
    :return: Aggregation operator
    """
    return {'$setIntersection': list(expressions)}


def SET_UNION(*expressions):
    """
    Takes two or more arrays and returns an array containing the elements that appear in any input array.
    https://docs.mongodb.com/manual/reference/operator/aggregation/setUnion/
    for more details
    :param expressions: The arrays (expressions)
    :return: Aggregation operator
    """
    return {'$setUnion': list(expressions)}


def SET_DIFFERENCE(*expressions):
    """
    Takes two sets and returns an array containing the elements that only exist in the first set.
    https://docs.mongodb.com/manual/reference/operator/aggregation/setDifference/
    for more details
    :param expressions: The arrays (expressions)
    :return: Aggregation operator
    """
    return {'$setDifference': list(expressions)}


def SET_IS_SUBSET(*expressions):
    """
    Takes two arrays and returns true when the first array is a subset of the second,
    including when the first array equals the second array, and false otherwise.
    https://docs.mongodb.com/manual/reference/operator/aggregation/setIsSubset/
    for more details
    :param expressions: The arrays (expressions)
    :return: Aggregation operator
    """
    return {'$setIsSubset': list(expressions)}


def ANY_ELEMENT_TRUE(*expressions):
    """
    Evaluates an array as a set and returns true if any of the elements are true and false otherwise.
    An empty array returns false.
    https://docs.mongodb.com/manual/reference/operator/aggregation/anyElementTrue/
    for more details
    :param expressions: The arrays (expressions)
    :return: Aggregation operator
    """
    return {'$anyElementTrue': list(expressions)}


def ALL_ELEMENTS_TRUE(*expressions):
    """
    Evaluates an array as a set and returns true if no element in the array is false. Otherwise, returns false.
    An empty array returns true.
    https://docs.mongodb.com/manual/reference/operator/aggregation/allElementsTrue/
    for more details
    :param expressions: The arrays (expressions)
    :return: Aggregation operator
    """
    return {'$allElementsTrue': list(expressions)}
