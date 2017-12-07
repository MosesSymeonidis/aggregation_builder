def AND(*expressions):
    return {'$and': list(expressions)}


def OR(*expressions):
    return {'$or': list(expressions)}


def NOT(expression):
    return {'$not': [expression]}
