from aggregation_builder import AggregationQueryBuilder
from aggregation_builder.Operators import *
import unittest
import datetime


class ArithmeticOperatorsTests(unittest.TestCase):
    def test_abs(self):
        query = [
            {
                '$project':
                    {
                        'delta': {'$abs': {'$subtract': ["$start", "$end"]}}
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            delta=ABS(SUBTRACT("$start", "$end"))
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_add_numbers(self):
        query = [
            {'$project': {'item': 1, 'total': {'$add': ["$price", "$fee"]}}}
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, total=ADD("$price", "$fee")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_add_on_a_date(self):
        query = [
            {'$project': {'item': 1, 'billing_date': {'$add': ["$date", 3 * 24 * 60 * 60000]}}}
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, billing_date=ADD("$date", 3 * 24 * 60 * 60000)
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_ceil(self):
        query = [
            {'$project': {'value': 1, 'ceilingValue': {'$ceil': "$value"}}}
        ]
        generated_query = AggregationQueryBuilder().project(
            value=1, ceilingValue=CEIL("$value")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_divide(self):
        query = [
            {'$project': {'name': 1, 'workdays': {'$divide': ["$hours", 8]}}}
        ]
        generated_query = AggregationQueryBuilder().project(
            name=1, workdays=DIVIDE("$hours", 8)
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_exp(self):
        query = [
            {'$project': {'effectiveRate': {'$subtract': [{'$exp': "$rate"}, 1]}}}
        ]
        generated_query = AggregationQueryBuilder().project(
            effectiveRate=SUBTRACT(EXP("$rate"), 1)
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_floor(self):
        query = [
            {'$project': {'value': 1, 'floorValue': {"$floor": "$value"}}}
        ]
        generated_query = AggregationQueryBuilder().project(
            value=1, floorValue=FLOOR("$value")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_ln(self):
        query = [
            {'$project': {'x': '$year', 'y': {"$ln": "$sales"}}}
        ]
        generated_query = AggregationQueryBuilder().project(
            x="$year", y=LN('$sales')
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_log(self):
        query = [
            {'$project': {'bitsNeeded':
                {
                    '$floor': {'$add': [1, {'$log': ["$positiveInt", 2]}]}}}
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            bitsNeeded=FLOOR(ADD(1, LOG("$positiveInt", 2)))
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_log10(self):
        query = [
            {'$project': {'pH':
                {
                    '$multiply': [-1, {'$log10': "$H3O"}]}}
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            pH=MULTIPLY(-1, LOG10("$H3O"))
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_mod(self):
        query = [
            {'$project': {'remainder':
                {
                    '$mod': ["$hours", "$tasks"]}}
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            remainder=MOD("$hours", "$tasks")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_multiply(self):
        query = [
            {'$project': {'date': 1, 'item': 1, 'total': {'$multiply': ["$price", "$quantity"]}}}
        ]

        generated_query = AggregationQueryBuilder().project(
            date=1, item=1, total=MULTIPLY("$price", "$quantity")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_pow(self):
        query = [
            {'$project': {'variance': {'$pow': [{'$stdDevPop': "$scores.score"}, 2]}}}
        ]

        generated_query = AggregationQueryBuilder().project(
            variance=POW(STD_DEV_POP("$scores.score"), 2)
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_sqrt(self):
        query = [
            {
                '$project': {
                    'distance': {
                        '$sqrt': {
                            '$add': [
                                {'$pow': [{'$subtract': ["$p2.y", "$p1.y"]}, 2]},
                                {'$pow': [{'$subtract': ["$p2.x", "$p1.x"]}, 2]}
                            ]
                        }
                    }
                }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            distance=SQRT(ADD(
                POW(SUBTRACT("$p2.y", "$p1.y"), 2),
                POW(SUBTRACT("$p2.x", "$p1.x"), 2)))
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_subtract_numbers(self):
        query = [{'$project': {'item': 1, 'total': {'$subtract': [{'$add': ["$price", "$fee"]}, "$discount"]}}}]

        generated_query = AggregationQueryBuilder().project(
            item=1,
            total=SUBTRACT(ADD("$price", "$fee"), "$discount")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_subtract_dates(self):
        date = datetime.datetime.now()

        query = [{'$project': {'item': 1, 'dateDifference': {'$subtract': [date, "$date"]}}}]

        generated_query = AggregationQueryBuilder().project(
            item=1,
            dateDifference=SUBTRACT(date, "$date")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_trunc(self):
        query = [{ '$project': { 'value': 1, 'truncatedValue': { '$trunc': "$value" } } }]

        generated_query = AggregationQueryBuilder().project(
            value=1,
            truncatedValue=TRUNC("$value")
        ).get_query()

        self.assertListEqual(generated_query, query)

if __name__ == '__main__':
    unittest.main()
