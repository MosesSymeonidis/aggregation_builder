def DAY_OF_YEAR(expression):
    return {'$dayOfYear': expression}


def DAY_OF_MONTH(expression):
    return {'$dayOfMonth': expression}


def DAY_OF_WEEK(expression):
    return {'$dayOfWeek': expression}


def YEAR(expression):
    return {'$year': expression}


def MONTH(expression):
    return {'$month': expression}


def WEEK(expression):
    return {'$week': expression}


def HOUR(expression):
    return {'$hour': expression}


def MINUTE(expression):
    return {'$minute': expression}


def SECOND(expression):
    return {'$second': expression}


def MILLISECOND(expression):
    return {'$millisecond': expression}


def DATE_TO_STRING(_format, date):
    return {'$dateToString': {'format': _format, 'date': date}}


def ISO_DAY_OF_WEEK(expression):
    return {'$isoDayOfWeek': expression}


def ISO_WEEK(expression):
    return {'$isoWeek': expression}


def ISO_WEEK_YEAR(expression):
    return {'$isoWeekYear': expression}
