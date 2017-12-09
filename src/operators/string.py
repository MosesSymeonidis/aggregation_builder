def CONCAT(*expressions):
    """
    Concatenates strings and returns the concatenated string.
    https://docs.mongodb.com/manual/reference/operator/aggregation/concat/
    for more details
    :param expressions: The list of strings (variables or expressions)
    :return: Aggregation operator
    """
    return {'$concat': list(expressions)}


def SPLIT(expression, delimiter):
    """
    Divides a string into an array of substrings based on a delimiter.
    https://docs.mongodb.com/manual/reference/operator/aggregation/split/
    for more details
    :param expression: The string or expression of the string
    :return: Aggregation operator
    """
    return {'$split': [expression, delimiter]}


def STR_LEN_BYTES(expression):
    """
    Returns the number of UTF-8 encoded bytes in the specified string.
    https://docs.mongodb.com/manual/reference/operator/aggregation/strLenBytes/
    for more details
    :param expression: The string or expression of the string
    :return: Aggregation operator
    """
    return {'$strLenBytes': expression}


def STR_LEN_CP(expression):
    """
    Returns the number of UTF-8 code points in the specified string.
    https://docs.mongodb.com/manual/reference/operator/aggregation/strLenCP/
    for more details
    :param expression: The string or expression of the string
    :return: Aggregation operator
    """
    return {'$strLenCP': expression}


def STR_CASE_CMP(x, y):
    """
    Performs case-insensitive comparison of two strings. Returns
        1 if first string is “greater than” the second string.
        0 if the two strings are equal.
        -1 if the first string is “less than” the second string.

    https://docs.mongodb.com/manual/reference/operator/aggregation/strcasecmp/
    for more details
    :param x: The first string or expression of string
    :param y: The second string or expression of string
    :return: Aggregation operator
    """
    return {'$strcasecmp': [x, y]}


def SUB_STR(string, start, length):
    """
    Returns a substring of a string, starting at a specified index position
    and including the specified number of characters.
    https://docs.mongodb.com/manual/reference/operator/aggregation/substr/
    for more details
    :param string: The string or expression of string
    :param start: Indicates the starting point of the substring.
    :param length: Can be any valid expression as long as it resolves to a non-negative integer or number
    :return: Aggregation operator
    """
    return {'$substr': [string, start, length]}


def SUB_STR_BYTES(string, index, length):
    """
    Returns the substring of a string.
    The substring starts with the character at the specified UTF-8 byte index (zero-based) in the string
    and continues for the number of bytes specified.
    https://docs.mongodb.com/manual/reference/operator/aggregation/substrBytes/
    for more details
    :param string: The string or expression of string
    :param index: Indicates the starting point of the substring.
    :param length: Can be any valid expression as long as it resolves to a non-negative integer or number
    :return: Aggregation operator
    """
    return {'$substrBytes': [string, index, length]}


def SUB_STR_CP(string, index, count):
    """
    Returns the substring of a string.
    The substring starts with the character at the specified UTF-8 code point (CP) index (zero-based)
    in the string for the number of code points specified.
    https://docs.mongodb.com/manual/reference/operator/aggregation/substrCP/
    for more details
    :param string: The string or expression of string
    :param index: Indicates the starting point of the substring.
    :param length: Can be any valid expression as long as it resolves to a non-negative integer or number
    :return: Aggregation operator
    """
    return {'$substrCP': [string, index, count]}


def TO_LOWER(expression):
    """
    Converts a string to lowercase, returning the result.
    https://docs.mongodb.com/manual/reference/operator/aggregation/toLower/
    for more details
    :param expression: The string or expression of string
    :return: Aggregation operator
    """
    return {'$toLower': expression}


def TO_UPPER(expression):
    """
    Converts a string to uppercase, returning the result.
    https://docs.mongodb.com/manual/reference/operator/aggregation/toUpper/
    for more details
    :param expression: The string or expression of string
    :return: Aggregation operator
    """
    return {'$toUpper': expression}


def INDEX_OF_BYTES(string_expression, substring_expression, start=None, end=None):
    """
    Searches a string for an occurence of a substring and returns the UTF-8 byte index (zero-based) of the first occurence.
    If the substring is not found, returns -1.
    https://docs.mongodb.com/manual/reference/operator/aggregation/indexOfBytes/
    for more details
    :param string_expression: The string or expression of string
    :param substring_expression: The string or expression of substring
    :param start: An integral number (or expression) that specifies the starting index position for the search.
    :param end: An integral number (or expression) that specifies the ending index position for the search.
    :return: Aggregation operator
    """
    res = [string_expression, substring_expression]
    if start is not None:
        res.append(start)
    if end is not None:
        res.append(end)
    return {'$indexOfBytes': res}


def INDEX_OF_CP(string_expression, substring_expression, start=None, end=None):
    """
    Searches a string for an occurence of a substring and returns the UTF-8 code point index (zero-based) of the first occurence.
    If the substring is not found, returns -1.
    https://docs.mongodb.com/manual/reference/operator/aggregation/indexOfCP/
    for more details
    :param string_expression: The string or expression of string
    :param substring_expression: The string or expression of substring
    :param start: A number that can be represented as integers (or expression), that specifies the starting index position for the search.
    :param end: A number that can be represented as integers (or expression), that specifies the ending index position for the search.
    :return: Aggregation operator
    """
    res = [string_expression, substring_expression]
    if start is not None:
        res.append(start)
    if end is not None:
        res.append(end)
    return {'$indexOfCP': res}
