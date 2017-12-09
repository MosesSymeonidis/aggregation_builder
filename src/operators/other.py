def LET(_in, _vars):
    """
    Binds variables for use in the specified expression, and returns the result of the expression.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/let/
    for more details
    :param _in: The expression to evaluate.
    :param _vars: Assignment block for the variables accessible in the in expression.
    :return: Aggregation operator
    """
    return {'$let': {'vars': _vars, 'in': _in}}


def LITERAL(value):
    """
    Returns a value without parsing. Use for values that the aggregation pipeline may interpret as an expression.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/literal/
    for more details
    :param value: The expression or variable
    :return: Aggregation operator
    """
    return {'$literal': value}


def TYPE(expression):
    """
    Returns a string that specifies the BSON type of the argument.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/type/
    for more details
    :param expression: The expression or variable
    :return: Aggregation operator
    """
    return {'$type': expression}


def TEXT_SEARCH(text):
    """
    The $text operator assigns a score to each document that contains the search term in the indexed fields.
    The score represents the relevance of a document to a given text search query.
    See https://docs.mongodb.com/v3.4/tutorial/text-search-in-aggregation/
    for more details
    :param text: The text that you like to match-score
    :return: Aggregation operator
    """
    return {'$text': {'$search': text}}


TEXT_META = {'$meta': 'textScore'}
"""
    Helpful variable for sorting by score of text search operator
    See https://docs.mongodb.com/v3.4/tutorial/text-search-in-aggregation/
    for more details
"""


def COND(_if, _then, _else):
    """
    Evaluates a boolean expression to return one of the two specified return expressions.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/cond/
    for more details
    :param _if: expression that will be evaluated
    :param _then: if _if expression evaluates as true then COND operator returns _then statement
    :param _else: otherwise returns _else statement
    :return: Aggregation operator
    """
    return {'$cond': {'if': _if, 'then': _then, 'else': _else}}


def IF_NULL(expression, _else):
    """
    Evaluates an expression and returns the value of the expression if the expression evaluates to a non-null value.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/ifNull/
    for more details
    :param expression: expression that will be evaluated
    :param _else: value or expression if 'expression' is null
    :return:  Aggregation operator
    """
    return {'$ifNull': [expression, _else]}
