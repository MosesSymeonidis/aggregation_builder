from aggregation_builder import AggregationQueryBuilder
from aggregation_builder.operators import *
import unittest
import mongomock


class ExecutionTests(unittest.TestCase):
    def setUp(self):
        self.colection = mongomock.MongoClient().db.collection
        objects = [
            {'group_field': 0, 'sum_field': 15},
            {'group_field': 0, 'sum_field': 20},
            {'group_field': 1, 'sum_field': 30},
            {'group_field': 1, 'sum_field': 45},
            {'group_field': 0, 'sum_field': 82},
            {'group_field': 2, 'sum_field': 3},
            {'group_field': 1, 'sum_field': 56},
            {'group_field': 3, 'sum_field': 15},
            {'group_field': 4, 'sum_field': 20},
            {'group_field': 1, 'sum_field': 30},
            {'group_field': 2, 'sum_field': 45},
            {'group_field': 4, 'sum_field': 82},
            {'group_field': 3, 'sum_field': 3},
            {'group_field': 2, 'sum_field': 56}
        ]
        for obj in objects:
            self.colection.insert(obj)

    def test_main(self):
        query = [
            {
                '$group':
                    {
                        '_id': "$group_field",
                        'totalAmount': {'$sum': "$sum_field"}
                    }
            },
            {'$sort': {'totalAmount': 1}},
            {'$limit': 3}
        ]

        result_query_builder = AggregationQueryBuilder(self.colection).group(
            id="$group_field",
            totalAmount=SUM("$sum_field")
        ).sort(
            totalAmount=1
        ).limit(3).execute()
        result = self.colection.aggregate(
            query
        )

        self.assertListEqual([i for i in result_query_builder], [j for j in result])


if __name__ == '__main__':
    unittest.main()
