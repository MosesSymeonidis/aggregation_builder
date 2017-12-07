def CMP(x=None, y=None):
    if x is None and y is None:
        return {'$cmp': []}
    return {'$cmp': [x, y]}


def EQ(x=None, y=None):
    if x is None and y is None:
        return {'$eq': []}
    return {'$eq': [x, y]}


def GT(x=None, y=None):
    if x is None and y is None:
        return {'$gt': []}
    return {'$gt': [x, y]}


def GTE(x=None, y=None):
    if x is None and y is None:
        return {'$gte': []}
    return {'$gte': [x, y]}


def LT(x=None, y=None):
    if x is None and y is None:
        return {'$lt': []}
    return {'$lt': [x, y]}


def LTE(x=None, y=None):
    if x is None and y is None:
        return {'$lte': []}
    return {'$lte': [x, y]}


def NE(x=None, y=None):
    if x is None and y is None:
        return {'$ne': []}
    return {'$ne': [x, y]}
