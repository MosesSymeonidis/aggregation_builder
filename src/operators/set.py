def SET_EQUALS(*expressions):
    return {'$setEquals': list(expressions)}


def SET_INTERSECTION(*expressions):
    return {'$setIntersection': list(expressions)}


def SET_UNION(*expressions):
    return {'$setUnion': list(expressions)}


def SET_DIFFERENCE(*expressions):
    return {'$setDifference': list(expressions)}


def SET_IS_SUBSET(*expressions):
    return {'$setIsSubset': list(expressions)}


def ANY_ELEMENT_TRUE(*expressions):
    return {'$anyElementTrue': list(expressions)}


def ALL_ELEMENTS_TRUE(*expressions):
    return {'$allElementsTrue': list(expressions)}
