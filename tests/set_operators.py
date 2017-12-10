from aggregation_builder import AggregationQueryBuilder
from aggregation_builder.operators import *
import unittest


class SetOperatorsTests(unittest.TestCase):
    def test_set_equals(self):
        query = [
            {'$project': {'A': 1, 'B': 1, 'sameElements': {'$setEquals': ["$A", "$B"]}, '_id': 0}}
        ]
        generated_query = AggregationQueryBuilder().project(
            A=1, B=1, sameElements=SET_EQUALS("$A", "$B"), id=0
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_set_intersection(self):
        query = [
            {'$project': {'A': 1, 'B': 1, 'commonToBoth': {'$setIntersection': ["$A", "$B"]}, '_id': 0}}
        ]
        generated_query = AggregationQueryBuilder().project(
            A=1, B=1, commonToBoth=SET_INTERSECTION("$A", "$B"), id=0
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_set_union(self):
        query = [
            {'$project': {'A': 1, 'B': 1, 'allValues': {'$setUnion': ["$A", "$B"]}, '_id': 0}}
        ]
        generated_query = AggregationQueryBuilder().project(
            A=1, B=1, allValues=SET_UNION("$A", "$B"), id=0
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_set_difference(self):
        query = [
            {'$project': {'A': 1, 'B': 1, 'inBOnly': {'$setDifference': ["$B", "$A"]}, '_id': 0}}
        ]
        generated_query = AggregationQueryBuilder().project(
            A=1, B=1, inBOnly=SET_DIFFERENCE("$B","$A"), id=0
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_set_is_subset(self):
        query = [
            {'$project': {'A': 1, 'B': 1, 'AisSubset': {'$setIsSubset': ["$A", "$B"]}, '_id': 0}}
        ]
        generated_query = AggregationQueryBuilder().project(
            A=1, B=1, AisSubset=SET_IS_SUBSET("$A","$B"), id=0
        ).get_query()
        self.assertListEqual(generated_query, query)

    def test_any_element_true(self):
        query = [
            { '$project': {'responses': 1, 'isAnyTrue': { '$anyElementTrue': ["$responses"]}, '_id': 0}}
        ]
        generated_query = AggregationQueryBuilder().project(
            responses=1, isAnyTrue=ANY_ELEMENT_TRUE("$responses"), id=0
        ).get_query()
        self.assertListEqual(generated_query, query)

    def test_all_elements_true(self):
        query = [
            { '$project': {'responses': 1, 'isAllTrue': { '$allElementsTrue': ["$responses"]}, '_id': 0}}
        ]
        generated_query = AggregationQueryBuilder().project(
            responses=1, isAllTrue=ALL_ELEMENTS_TRUE("$responses"), id=0
        ).get_query()
        self.assertListEqual(generated_query, query)

if __name__ == '__main__':
    unittest.main()
