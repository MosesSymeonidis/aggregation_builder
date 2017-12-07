def ARRAY_ELEM_AT(array, idx):
    return {'$arrayElemAt': [array, idx]}


def ARRAY_TO_OBJECT(expression):
    return {'$arrayToObject': expression}


def CONCAT_ARRAYS(*arrays):
    return {'$concatArrays': list(arrays)}


def FILTER(_input, _as, cond):
    return {'$filter': {'input': _input, 'as': _as, 'cond': cond}}


def IN(expression, expressions):
    return {'$in': [expression, expressions]}


def IS_ARRAY(expression):
    return {'$isArray': expression}


def MAP(_input, _as, _in):
    return {'$map': {'input': _input, 'as': _as, 'in': _in}}


def OBJECT_TO_ARRAY(_object):
    return {'$objectToArray': _object}


def RANGE(start, end, step=None):
    return {'$range': [start, end, step]} if step is not None else {'$range': [start, end]}


def REDUCE(_input, initial_value, _in):
    return {'$reduce': {'input': _input, 'initialValue': initial_value, 'in': _in}}


def REVERSE_ARRAY(expression):
    return {'$reverseArray': expression}


def SIZE(expression):
    return {'$size': expression}


def SLICE(array, n, position=None):
    return {'$slice': [array, position, n]} if position is not None else {'$slice': [array, n]}


def ZIP(inputs, use_longest_length=None, defaults=None):
    res = {'inputs': inputs}
    if use_longest_length in [True, False]:
        res['useLongestLength'] = use_longest_length
    if defaults is not None:
        res['defaults'] = defaults
    return {'$zip': res}


def INDEX_OF_ARRAY(string_expression, substring_expression, start=None, end=None):
    res = [string_expression, substring_expression]
    if start is not None:
        res.append(start)
    if end is not None:
        res.append(end)
    return {'$indexOfArray': res}
