import mongomock
from datetime import datetime
from aggregation_builder import AggregationQueryBuilder
from aggregation_builder.operators import *
import unittest


def ISODate(str):
    return datetime.strptime(str, '%Y-%m-%dT%H:%M:%SZ')


class QueryDictTests(unittest.TestCase):
    def test_limit(self):
        query = [
            {
                '$limit': 5
            }
        ]
        generated_query = AggregationQueryBuilder().limit(5).get_query()

        self.assertListEqual(generated_query, query)

    def test_skip(self):
        query = [
            {
                '$skip': 5
            }
        ]
        generated_query = AggregationQueryBuilder().skip(5).get_query()

        self.assertListEqual(generated_query, query)

    def test_project(self):
        query = [{'$project': {'title': 1, 'author': 1}}]
        generated_query = AggregationQueryBuilder().project(title=1, author=1).get_query()

        self.assertListEqual(generated_query, query)

    def test_project_computed_fields(self):
        query = [
            {
                '$project': {
                    'title': 1,
                    'isbn': {
                        'prefix': {'$substr': ["$isbn", 0, 3]},
                        'group': {'$substr': ["$isbn", 3, 2]},
                        'publisher': {'$substr': ["$isbn", 5, 4]},
                        'title': {'$substr': ["$isbn", 9, 3]},
                        'checkDigit': {'$substr': ["$isbn", 12, 1]}
                    },
                    'lastName': "$author.last",
                    'copiesSold': "$copies"
                }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            title=1,
            isbn=dict(
                prefix=SUB_STR("$isbn", 0, 3),
                group=SUB_STR("$isbn", 3, 2),
                publisher=SUB_STR("$isbn", 5, 4),
                title=SUB_STR("$isbn", 9, 3),
                checkDigit=SUB_STR("$isbn", 12, 1)
            ),
            lastName="$author.last",
            copiesSold="$copies"

        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_match(self):
        query = [
            {
                '$match': {'author': "dave"}
            }
        ]
        generated_query = AggregationQueryBuilder().match(
            author="dave"
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_match_count(self):
        query = [
            {'$match': {'$or': [{'$gt': ["$score", 70]}, {'$gte': ["$views", 1000]}]}},
            {'$group': {'_id': None, 'count': {'$sum': 1}}}
        ]
        generated_query = AggregationQueryBuilder().match(
            OR(GT('$score', 70), GTE('$views', 1000))
        ).group(id=None, count=SUM(1)).get_query()

        self.assertListEqual(generated_query, query)

    def test_unwind(self):
        query = [{'$unwind': "$sizes"}]
        generated_query = AggregationQueryBuilder().unwind(
            "$sizes"
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_unwind_with_params(self):
        query = [{'$unwind': "$sizes", 'preserveNullAndEmptyArrays': True, 'includeArrayIndex': "arrayIndex"}]
        generated_query = AggregationQueryBuilder().unwind(
            path="$sizes",
            include_array_index="arrayIndex",
            preserve_null_and_empty_arrays=True
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_sort(self):
        query = [
            {'$sort': {'age': -1, 'posts': 1}}
        ]
        generated_query = AggregationQueryBuilder().sort(age=-1, posts=1).get_query()

        self.assertListEqual(generated_query, query)

    def test_sort_metadata(self):
        query = [
            {'$match': {'$text': {'$search': "operating"}}},
            {'$sort': {'score': {'$meta': "textScore"}, 'posts': -1}}
        ]
        generated_query = AggregationQueryBuilder().match(
            TEXT_SEARCH("operating")
        ).sort(
            score=TEXT_META,
            posts=-1
        ).get_query()
        self.assertListEqual(generated_query, query)

    def test_sample(self):
        query = [{'$sample': {'size': 3}}]
        generated_query = AggregationQueryBuilder().sample(size=3).get_query()
        self.assertListEqual(generated_query, query)

    def test_lookup(self):
        query = [
            {
                '$lookup':
                    {
                        'from': "inventory",
                        'localField': "item",
                        'foreignField': "sku",
                        'as': "inventory_docs"
                    }
            }
        ]

        generated_query = AggregationQueryBuilder().look_up(
            _from='inventory',
            _localField='item',
            _foreignField='sku',
            _as='inventory_docs'
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_lookup_with_array(self):
        query = [
            {
                '$unwind': "$specs"
            },
            {
                '$lookup':
                    {
                        'from': "inventory",
                        'localField': "specs",
                        'foreignField': "size",
                        'as': "inventory_docs"
                    }
            },
            {
                '$match': {"inventory_docs": {'$ne': []}}
            }
        ]

        generated_query = AggregationQueryBuilder().unwind(
            "$specs"
        ).look_up(
            _from='inventory',
            _localField='specs',
            _foreignField='size',
            _as='inventory_docs'
        ).match(
            inventory_docs=NE()
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_graph_look_up(self):
        query = [
            {
                '$graphLookup': {
                    'from': "employees",
                    'startWith': "$reportsTo",
                    'connectFromField': "reportsTo",
                    'connectToField': "name",
                    'as': "reportingHierarchy"
                }
            }
        ]
        generated_query = AggregationQueryBuilder().graph_look_up(
            _from='employees',
            _startWith="$reportsTo",
            _connectFromField="reportsTo",
            _connectToField="name",
            _as="reportingHierarchy"
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_add_fields(self):
        query = [
            {
                '$addFields': {
                    'totalHomework': {'$sum': "$homework"},
                    'totalQuiz': {'$sum': "$quiz"}
                }
            },
            {
                '$addFields': {'totalScore':
                                   {'$add': ["$totalHomework", "$totalQuiz", "$extraCredit"]}}
            }
        ]
        generated_query = AggregationQueryBuilder().add_fields(
            totalHomework=SUM("$homework"),
            totalQuiz=SUM("$quiz")
        ).add_fields(
            totalScore=ADD("$totalHomework", "$totalQuiz", "$extraCredit")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_group(self):
        query = [
            {
                '$group': {
                    '_id': {'month': {'$month': "$date"}, 'day': {'$dayOfMonth': "$date"}, 'year': {'$year': "$date"}},
                    'totalPrice': {'$sum': {'$multiply': ["$price", "$quantity"]}},
                    'averageQuantity': {'$avg': "$quantity"},
                    'count': {'$sum': 1}
                }
            }
        ]

        generated_query = AggregationQueryBuilder().group(
            id=dict(
                month=MONTH("$date"),
                day=DAY_OF_MONTH("$date"),
                year=YEAR("$date")
            ),
            totalPrice=SUM(MULTIPLY("$price", "$quantity")),
            averageQuantity=AVG("$quantity"),
            count=SUM(1)
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_null_group(self):
        query = [
            {
                '$group': {
                    '_id': None,
                    'totalPrice': {'$sum': {'$multiply': ["$price", "$quantity"]}},
                    'averageQuantity': {'$avg': "$quantity"},
                    'count': {'$sum': 1}
                }
            }
        ]

        generated_query = AggregationQueryBuilder().group(
            id=None,
            totalPrice=SUM(MULTIPLY("$price", "$quantity")),
            averageQuantity=AVG("$quantity"),
            count=SUM(1)
        ).get_query()

        self.assertListEqual(generated_query, query)


if __name__ == '__main__':
    unittest.main()
