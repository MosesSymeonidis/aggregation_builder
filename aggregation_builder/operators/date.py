def DAY_OF_YEAR(expression):
    """
    Returns the day of the year for a date as a number between 1 and 366.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfYear/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$dayOfYear': expression}


def DAY_OF_MONTH(expression):
    """
    Returns the day of the month for a date as a number between 1 and 31.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$dayOfMonth': expression}


def DAY_OF_WEEK(expression):
    """
    Returns the day of the week for a date as a number between 1 (Sunday) and 7 (Saturday).
    See https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfWeek/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$dayOfWeek': expression}


def YEAR(expression):
    """
    Returns the year portion of a date.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/year/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$year': expression}


def MONTH(expression):
    """
    Returns the month of a date as a number between 1 and 12.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/month/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$month': expression}


def WEEK(expression):
    """
    Returns the week of the year for a date as a number between 0 and 53.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/week/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$week': expression}


def HOUR(expression):
    """
    Returns the hour portion of a date as a number between 0 and 23.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/hour/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$hour': expression}


def MINUTE(expression):
    """
    Returns the minute portion of a date as a number between 0 and 59.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/minute/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$minute': expression}


def SECOND(expression):
    """
    Returns the second portion of a date as a number between 0 and 59, but can be 60 to account for leap seconds.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/minute/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$second': expression}


def MILLISECOND(expression):
    """
    Returns the millisecond portion of a date as an integer between 0 and 999.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/millisecond/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$millisecond': expression}


def DATE_TO_STRING(_format, date):
    """
    Converts a date object to a string according to a user-specified format.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/dateToString/
    for more details
    :param _format: The date format specification.
    :param date: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$dateToString': {'format': _format, 'date': date}}


def ISO_DAY_OF_WEEK(expression):
    """
    Returns the weekday number in ISO 8601 format, ranging from 1 (for Monday) to 7 (for Sunday).
    See https://docs.mongodb.com/manual/reference/operator/aggregation/isoDayOfWeek/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$isoDayOfWeek': expression}


def ISO_WEEK(expression):
    """
    Returns the week number in ISO 8601 format, ranging from 1 to 53.
    Week numbers start at 1 with the week (Monday through Sunday) that contains the year’s first Thursday.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/isoWeek/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$isoWeek': expression}


def ISO_WEEK_YEAR(expression):
    """
    Returns the year number in ISO 8601 format.
    The year starts with the Monday of week 1 and ends with the Sunday of the last week.
    See https://docs.mongodb.com/manual/reference/operator/aggregation/isoWeekYear/
    for more details
    :param expression: expression or variable of a Date, a Timestamp, or an ObjectID
    :return: Aggregation operator
    """
    return {'$isoWeekYear': expression}
