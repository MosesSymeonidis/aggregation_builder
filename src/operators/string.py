def CONCAT(*expressions):
    return {'$concat': list(expressions)}


def SPLIT(expression, delimiter):
    return {'$split': [expression, delimiter]}


def STR_LEN_BYTES(expression):
    return {'$strLenBytes': expression}


def STR_LEN_CP(expression):
    return {'$strLenCP': expression}


def STR_CASE_CMP(x, y):
    return {'$strcasecmp': [x, y]}


def SUB_STR(string, start, length):
    return {'$substr': [string, start, length]}


def SUB_STR_BYTES(string, index, length):
    return {'$substrBytes': [string, index, length]}


def SUB_STR_CP(string, index, count):
    return {'$substrCP': [string, index, count]}


def TO_LOWER(expression):
    return {'$toLower': expression}


def TO_UPPER(expression):
    return {'$toUpper': expression}


def INDEX_OF_BYTES(string_expression, substring_expression, start=None, end=None):
    res = [string_expression, substring_expression]
    if start is not None:
        res.append(start)
    if end is not None:
        res.append(end)
    return {'$indexOfBytes': res}


def INDEX_OF_CP(string_expression, substring_expression, start=None, end=None):
    res = [string_expression, substring_expression]
    if start is not None:
        res.append(start)
    if end is not None:
        res.append(end)
    return {'$indexOfCP': res}
