def ARRAY_ELEM_AT(array, idx):
    """
    Returns the element at the specified array index.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/arrayElemAt/
    for more details
    :param array: An expression that can be any valid expression as long as it resolves to an array.
    :param idx: An expression can be any valid expression as long as it resolves to an integer.
    :return: Aggregation operator
    """
    return {'$arrayElemAt': [array, idx]}


def ARRAY_TO_OBJECT(expression):
    """
    Converts an array into a single document.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/arrayToObject/
    for more details
    :param expression: An expression that can be any valid expression as long as it resolves to an array.
    :return: Aggregation operator
    """
    return {'$arrayToObject': expression}


def CONCAT_ARRAYS(*arrays):
    """
    Concatenates arrays to return the concatenated array.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/concatArrays/
    for more details
    :param arrays: A set of arrays(expressions).
    :return: Aggregation operator
    """
    return {'$concatArrays': list(arrays)}


def FILTER(_input, _as, cond):
    """
    Selects a subset of an array to return based on the specified condition. \
    Returns an array with only those elements that match the condition.
    The returned elements are in the original order.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/filter/
    for more details
    :param _input: An expression that resolves to an array.
    :param _as: A name for the variable that represents each individual element of the input array.
    :param cond: An expression that resolves to a boolean value used to determine if an element should be included in the output array.
    :return: Aggregation operator
    """
    return {'$filter': {'input': _input, 'as': _as, 'cond': cond}}


def IN(expression, expressions):
    """
    Returns a boolean indicating whether a specified value is in an array.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/in/
    for more details
    :param expression: Any valid expression.
    :param expressions: Any valid expression that resolves to an array.
    :return: Aggregation operator
    """
    return {'$in': [expression, expressions]}


def IS_ARRAY(expression):
    """
    Determines if the operand is an array. Returns a boolean.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/isArray/
    for more details
    :param expression: Any valid expression.
    :return: Aggregation operator
    """
    return {'$isArray': expression}


def MAP(_input, _as, _in):
    """
    Applies an expression to each item in an array and returns an array with the applied results.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/map/
    for more details
    :param _input: An expression that resolves to an array.
    :param _as: A name for the variable that represents each individual element of the input array.
    :param _in: An expression that is applied to each element of the input array.
    :return: Aggregation operator
    """
    return {'$map': {'input': _input, 'as': _as, 'in': _in}}


def OBJECT_TO_ARRAY(_object):
    """
    Converts a document to an array. The return array contains a element for each field/value pair in the original document.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/objectToArray/
    for more details
    :param _object: can be any valid expression as long as it resolves to a document object.
    :return: Aggregation operator
    """
    return {'$objectToArray': _object}


def RANGE(start, end, step=None):
    """
    Generates the sequence from the specified starting number by successively
    incrementing the starting number by the specified step value up to but not including the end point.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/range/
    for more details
    :param start: An integer (or valid expression) that specifies the start of the sequence.
    :param end: An integer (or valid expression) that specifies the exclusive upper limit of the sequence.
    :param step: An integer (or valid expression) that specifies the increment value.
    :return: Aggregation operator
    """
    return {'$range': [start, end, step]} if step is not None else {'$range': [start, end]}


def REDUCE(_input, initial_value, _in):
    """
    Applies an expression to each element in an array and combines them into a single value.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/reduce/
    for more details
    :param _input: Can be any valid expression that resolves to an array.
    :param initial_value: The initial cumulative value set before in is applied to the first element of the input array.
    :param _in: A valid expression that reduce applies to each element in the input array in left-to-right order.
    :return: Aggregation operator
    """
    return {'$reduce': {'input': _input, 'initialValue': initial_value, 'in': _in}}


def REVERSE_ARRAY(expression):
    """
    Accepts an array expression as an argument and returns an array with the elements in reverse order.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/reverseArray/
    for more details
    :param expression: Any valid expression as long as it resolves to an array.
    :return: Aggregation operator
    """
    return {'$reverseArray': expression}


def SIZE(expression):
    """
    Counts and returns the total the number of items in an array.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/size/
    for more details
    :param expression: Any expression as long as it resolves to an array
    :return: Aggregation operator
    """
    return {'$size': expression}


def SLICE(array, n, position=None):
    """
    Returns a subset of an array.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/slice/
    for more details
    :param array: Any valid expression as long as it resolves to an array.
    :param n: Any valid expression as long as it resolves to an integer.
    :param position: Optional. Any valid expression as long as it resolves to an integer.
    :return: Aggregation operator
    """
    return {'$slice': [array, position, n]} if position is not None else {'$slice': [array, n]}


def ZIP(inputs, use_longest_length=None, defaults=None):
    """
    Transposes an array of input arrays so that the first element of the output array would be an array containing,
    the first element of the first input array,
    the first element of the second input array, etc.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/zip/
    for more details
    :param inputs: An array of expressions that resolve to arrays.
    :param use_longest_length: A boolean which specifies whether the length of the longest array determines the number of arrays in the output array.
    :param defaults: An array of default element values to use if the input arrays have different lengths.
    :return: Aggregation operator
    """
    res = {'inputs': inputs}
    if use_longest_length in [True, False]:
        res['useLongestLength'] = use_longest_length
    if defaults is not None:
        res['defaults'] = defaults
    return {'$zip': res}


def INDEX_OF_ARRAY(string_expression, substring_expression, start=None, end=None):
    """
    Searches an array for an occurence of a specified value and returns the array index of the first occurence.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/zip/
    for more details
    :param string_expression: Any valid expression as long as it resolves to an array.
    :param substring_expression: Can be any valid expression.
    :param start: A number that can be represented as integers that specifies the starting index position for the search.
    :param end: A number that can be represented as integers that specifies the ending index position for the search.
    :return: Aggregation operator
    """
    res = [string_expression, substring_expression]
    if start is not None:
        res.append(start)
    if end is not None:
        res.append(end)
    return {'$indexOfArray': res}
