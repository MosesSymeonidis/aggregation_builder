from aggregation_builder import AggregationQueryBuilder
from aggregation_builder.operators import *
import unittest
import datetime


class ArithmeticOperatorsTests(unittest.TestCase):
    def test_dates(self):
        query = [
            {
                '$project':
                    {
                        'year': {'$year': "$date"},
                        'month': {'$month': "$date"},
                        'day': {'$dayOfMonth': "$date"},
                        'hour': {'$hour': "$date"},
                        'minutes': {'$minute': "$date"},
                        'seconds': {'$second': "$date"},
                        'milliseconds': {'$millisecond': "$date"},
                        'dayOfYear': {'$dayOfYear': "$date"},
                        'dayOfWeek': {'$dayOfWeek': "$date"},
                        'week': {'$week': "$date"}
                    }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            year=YEAR('$date'),
            month=MONTH('$date'),
            day=DAY_OF_MONTH('$date'),
            hour=HOUR('$date'),
            minutes=MINUTE('$date'),
            seconds=SECOND('$date'),
            milliseconds=MILLISECOND('$date'),
            dayOfYear=DAY_OF_YEAR('$date'),
            dayOfWeek=DAY_OF_WEEK('$date'),
            week=WEEK('$date')
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_date_to_string(self):
        query = [
            {
                '$project':
                    {
                        'yearMonthDayUTC': {'$dateToString': {'format': "%Y-%m-%d", 'date': "$date"}},
                        'time': {'$dateToString': {'format': "%H:%M:%S:%L", 'date': "$date"}}
                    }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            yearMonthDayUTC=DATE_TO_STRING(_format="%Y-%m-%d", date="$date"),
            time=DATE_TO_STRING(_format="%H:%M:%S:%L", date="$date")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_iso_day_of_week(self):
        query = [
            {
                '$project':
                    {
                        '_id': 0,
                        'name': "$name",
                        'dayOfWeek': { '$isoDayOfWeek': "$birthday"}
                    }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            id=0,
            name="$name",
            dayOfWeek=ISO_DAY_OF_WEEK("$birthday")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_iso_week(self):
        query = [
            {
                '$project':
                    {
                        '_id': 0,
                        'city': "$city",
                        'weekNumber': { '$isoWeek': "$birthday"}
                    }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            id=0,
            city="$city",
            weekNumber=ISO_WEEK("$birthday")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_iso_week_year(self):
        query = [
            {
                '$project':
                    {
                        'yearNumber': { '$isoWeekYear': "$birthday"}
                    }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            yearNumber=ISO_WEEK_YEAR("$birthday")
        ).get_query()

        self.assertListEqual(generated_query, query)

if __name__ == '__main__':
    unittest.main()
