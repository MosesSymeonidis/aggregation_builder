from Utils.AggregationBuilder.AggregationBuilder import AggregationQueryBuilder
from Utils.AggregationBuilder.Operators import *
import unittest
import datetime


class OtherOperatorsTests(unittest.TestCase):
    def test_text(self):
        query = [
            {'$match': {'$text': {'$search': "cake"}}},
            {'$group': {'_id': {'$meta': "textScore"}, 'count': {'$sum': 1}}}
        ]

        generated_query = AggregationQueryBuilder().match(
            **TEXT_SEARCH("cake")
        ).group(id=TEXT_META, count=SUM(1)).get_query()

        self.assertListEqual(generated_query, query)

    def test_let(self):
        query = [
            {
                '$project': {
                    'finalTotal': {
                        '$let': {
                            'vars': {
                                'total': {'$add': ['$price', '$tax']},
                                'discounted': {'$cond': {'if': '$applyDiscount', 'then': 0.9, 'else': 1}}
                            },
                            'in': {'$multiply': ["$$total", "$$discounted"]}
                        }
                    }
                }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            finalTotal=LET(
                _vars=dict(
                    total=ADD('$price', '$tax'),
                    discounted=COND(
                        _if='$applyDiscount',
                        _then=0.9,
                        _else=1
                    )
                ),
                _in=MULTIPLY("$$total", "$$discounted")
            )
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_literal(self):
        query = [
            {'$project': {'item': 1, 'startAt': {'$literal': 1}}}
        ]

        generated_query = AggregationQueryBuilder().project(
            item=1, startAt=LITERAL(1)
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_type(self):
        query = [
            {'$project': {'a': {'$type': "$a"}}}
        ]

        generated_query = AggregationQueryBuilder().project(
            a=TYPE('$a')
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_if_null(self):
        query = [
            {'$project': {
                'item': 1,
                'description': {'$ifNull': ["$description", "Unspecified"]}
            }}
        ]

        generated_query = AggregationQueryBuilder().project(
            item=1, description=IF_NULL("$description", "Unspecified")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_cond(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'discount':
                            {
                                '$cond': {'if': {'$gte': ["$qty", 250]}, 'then': 30, 'else': 20}
                            }
                    }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            item=1, discount=COND(_if=GTE("$qty", 250), _then=30,
                                  _else=20)
        ).get_query()

        self.assertListEqual(generated_query, query)


if __name__ == '__main__':
    unittest.main()
