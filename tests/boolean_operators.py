from Utils.AggregationBuilder.AggregationBuilder import AggregationQueryBuilder
from Utils.AggregationBuilder.Operators import *
import unittest
import datetime


class BooleanOperatorsTests(unittest.TestCase):
    def test_and(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'qty': 1,
                        'result': {'$and': [{'$gt': ["$qty", 100]}, {'$lt': ["$qty", 250]}]}
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, qty=1, result=AND(GT("$qty", 100), LT("$qty", 250))
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_or(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'result': {'$or': [{'$gt': ["$qty", 250]}, {'$lt': ["$qty", 200]}]}
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, result=OR(GT("$qty", 250), LT("$qty", 200))
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_not(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'result': {'$not': [{'$gt': ["$qty", 250]}]}
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, result=NOT(GT("$qty", 250))
        ).get_query()

        self.assertListEqual(generated_query, query)


if __name__ == '__main__':
    unittest.main()
