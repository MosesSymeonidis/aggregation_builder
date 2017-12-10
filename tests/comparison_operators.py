from aggregation_builder import AggregationQueryBuilder
from aggregation_builder.operators import *
import unittest
import datetime


class ArithmeticOperatorsTests(unittest.TestCase):
    def test_cmp(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'qty': 1,
                        'cmpTo250': {'$cmp': ["$qty", 250]},
                        '_id': 0
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, qty=1, cmpTo250=CMP("$qty", 250), id=0
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_eq(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'qty': 1,
                        'qtyEq250': {'$eq': ["$qty", 250]},
                        '_id': 0
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, qty=1, qtyEq250=EQ("$qty", 250), id=0
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_gt(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'qty': 1,
                        'qtyGt250': {'$gt': ["$qty", 250]},
                        '_id': 0
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, qty=1, qtyGt250=GT("$qty", 250), id=0
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_gte(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'qty': 1,
                        'qtyGte250': {'$gte': ["$qty", 250]},
                        '_id': 0
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, qty=1, qtyGte250=GTE("$qty", 250), id=0
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_lt(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'qty': 1,
                        'qtyLt250': {'$lt': ["$qty", 250]},
                        '_id': 0
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, qty=1, qtyLt250=LT("$qty", 250), id=0
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_lte(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'qty': 1,
                        'qtyLte250': {'$lte': ["$qty", 250]},
                        '_id': 0
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, qty=1, qtyLte250=LTE("$qty", 250), id=0
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_ne(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'qty': 1,
                        'qtyNe250': {'$ne': ["$qty", 250]},
                        '_id': 0
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, qty=1, qtyNe250=NE("$qty", 250), id=0
        ).get_query()

        self.assertListEqual(generated_query, query)



if __name__ == '__main__':
    unittest.main()
