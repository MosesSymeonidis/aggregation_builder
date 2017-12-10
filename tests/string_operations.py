from aggregation_builder import AggregationQueryBuilder
from aggregation_builder.operators import *
import unittest


class StringOperatorsTests(unittest.TestCase):
    def test_concat(self):
        query = [
            {'$project': {'itemDescription': {'$concat': ["$item", " - ", "$description"]}}}
        ]
        generated_query = AggregationQueryBuilder().project(
            itemDescription=CONCAT("$item", " - ", "$description")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_index_of_bytes(self):
        query = [
            {'$project': {
                'byteLocation': {'$indexOfBytes': ["$item", "foo"]},
            }}
        ]
        generated_query = AggregationQueryBuilder().project(
            byteLocation=INDEX_OF_BYTES("$item", "foo")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_index_of_cp(self):
        query = [
            {'$project': {
                'cpLocation': {'$indexOfCP': ["$item", "foo"]},
            }}
        ]
        generated_query = AggregationQueryBuilder().project(
            cpLocation=INDEX_OF_CP("$item", "foo")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_index_of_split(self):
        query = [
            {'$project': {'city_state': {'$split': ["$city", ", "]}, 'qty': 1}},
            {'$unwind': "$city_state"},
            {'$match': {'city_state': '/ [A - Z]{2} /'}},
            {'$group': {'_id': {"state": "$city_state"}, 'total_qty': {"$sum": "$qty"}}},
            {'$sort': {'total_qty': -1}}
        ]
        generated_query = AggregationQueryBuilder().project(
            city_state=SPLIT("$city", ", "), qty=1
        ).unwind(
            "$city_state"
        ).match(
            city_state='/ [A - Z]{2} /'
        ).group(
            id=dict(state="$city_state"), total_qty=SUM('$qty')
        ).sort(
            total_qty=-1
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_index_of_str_len_bytes(self):
        query = [
            {'$project': {
                'name': 1,
                'length': {'$strLenBytes': "$name"},
            }}
        ]
        generated_query = AggregationQueryBuilder().project(
            name=1, length=STR_LEN_BYTES("$name")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_index_of_str_len_cp(self):
        query = [
            {'$project': {
                'name': 1,
                'length': {'$strLenCP': "$name"},
            }}
        ]
        generated_query = AggregationQueryBuilder().project(
            name=1, length=STR_LEN_CP("$name")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_strcasecmp(self):
        query = [
            {'$project': {
                'item': 1,
                'comparisonResult': {'$strcasecmp': ["$quarter", "13q4"]},
            }}
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, comparisonResult=STR_CASE_CMP("$quarter", "13q4")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_substr(self):
        query = [
            {'$project': {
                'item': 1,
                'yearSubstring': {'$substr': ["$quarter", 0, 2]},
                'quarterSubtring': {'$substr': ["$quarter", 2, -1]}
            }}
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1, yearSubstring=SUB_STR("$quarter", 0, 2), quarterSubtring=SUB_STR("$quarter", 2, -1)
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_substr_bytes(self):
        query = [
            {'$project': {
                'item': 1,
                'yearSubstring': {'$substrBytes': ["$quarter", 0, 2]},
                'quarterSubtring': {
                    '$substrBytes': [
                        "$quarter", 2, {'$subtract': [{'$strLenBytes': "$quarter"}, 2]}
                    ]
                }
            }}
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1,
            yearSubstring=SUB_STR_BYTES("$quarter", 0, 2),
            quarterSubtring=SUB_STR_BYTES("$quarter", 2, SUBTRACT(STR_LEN_BYTES("$quarter"), 2))
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_substr_cp(self):
        query = [
            {'$project': {
                'item': 1,
                'yearSubstring': {'$substrCP': ["$quarter", 0, 2]},
                'quarterSubtring': {
                    '$substrCP': [
                        "$quarter", 2, {'$subtract': [{'$strLenCP': "$quarter"}, 2]}
                    ]
                }
            }}
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1,
            yearSubstring=SUB_STR_CP("$quarter", 0, 2),
            quarterSubtring=SUB_STR_CP("$quarter", 2, SUBTRACT(STR_LEN_CP("$quarter"), 2))
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_to_lower(self):
        query = [
            {'$project': {
                'item': {'$toLower': "$item"},
                'description': {'$toLower': "$description"}
            }}
        ]
        generated_query = AggregationQueryBuilder().project(
            item=TO_LOWER("$item"),
            description=TO_LOWER("$description")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_to_upper(self):
        query = [
            {'$project': {
                'item': {'$toUpper': "$item"},
                'description': {'$toUpper': "$description"}
            }}
        ]
        generated_query = AggregationQueryBuilder().project(
            item=TO_UPPER("$item"),
            description=TO_UPPER("$description")
        ).get_query()

        self.assertListEqual(generated_query, query)


if __name__ == '__main__':
    unittest.main()
