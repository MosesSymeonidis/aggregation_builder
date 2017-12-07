def LET(_in, _vars):
    return {'$let': {'vars': _vars, 'in': _in}}


def LITERAL(value):
    return {'$literal': value}


def TYPE(expression):
    return {'$type': expression}


def TEXT_SEARCH(text):
    return {'$text': {'$search': text}}


TEXT_META = {'$meta': 'textScore'}


def COND(_if, _then, _else):
    return {'$cond': {'if': _if, 'then': _then, 'else': _else}}


def IF_NULL(expression, _else):
    return {'$ifNull': [expression, _else]}
