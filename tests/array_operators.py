from Utils.AggregationBuilder.AggregationBuilder import AggregationQueryBuilder
from Utils.AggregationBuilder.Operators import *
import unittest


class ArrayOperatorsTests(unittest.TestCase):
    def test_arrayElemAt(self):
        query = [
            {
                '$project':
                    {
                        'name': 1,
                        'first': {'$arrayElemAt': ["$favorites", 0]},
                        'last': {'$arrayElemAt': ["$favorites", -1]}
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            name=1,
            first=ARRAY_ELEM_AT("$favorites", 0),
            last=ARRAY_ELEM_AT("$favorites", -1)
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_array_to_object(self):
        query = [
            {
                '$project':
                    {
                        'item': 1,
                        'dimensions': {'$arrayToObject': "$dimensions"},
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            item=1,
            dimensions=ARRAY_TO_OBJECT("$dimensions")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_object_to_array_and_array_to_object(self):
        query = [
            {'$addFields': {'instock': {'$objectToArray': "$instock"}}},
            {'$addFields': {'instock': {'$concatArrays': ["$instock", [{"k": "total", "v": {'$sum': "$instock.v"}}]]}}},
            {'$addFields': {'instock': {'$arrayToObject': "$instock"}}}
        ]
        generated_query = AggregationQueryBuilder().add_fields(
            instock=OBJECT_TO_ARRAY('$instock')
        ).add_fields(instock=CONCAT_ARRAYS("$instock", [dict(k="total", v=SUM("$instock.v"))])
                     ).add_fields(instock=ARRAY_TO_OBJECT("$instock")).get_query()
        self.assertListEqual(generated_query, query)

    def test_concat_arrays(self):
        query = [
            {'$project': {'items': {'$concatArrays': ["$instock", "$ordered"]}}}
        ]
        generated_query = AggregationQueryBuilder().project(
            items=CONCAT_ARRAYS("$instock", '$ordered')
        ).get_query()
        self.assertListEqual(generated_query, query)

    def test_filter_arrays(self):
        query = [
            {
                '$project': {
                    'items': {
                        '$filter': {
                            'input': "$items",
                            'as': "item",
                            'cond': {'$gte': ["$$item.price", 100]}
                        }
                    }
                }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            items=FILTER(
                _input="$items",
                _as="item",
                cond=GTE("$$item.price", 100)
            )
        ).get_query()
        self.assertListEqual(generated_query, query)

    def test_in_arrays(self):
        query = [
            {
                '$project': {
                    "store_location": "$location",
                    "has_bananas": {
                        '$in': ["bananas", "$in_stock"]
                    }
                }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            store_location='$location',
            has_bananas=IN("bananas", "$in_stock")
        ).get_query()
        self.assertListEqual(generated_query, query)

    def test_index_of_array(self):
        query = [
            {
                "$project":
                    {
                        "index": {"$indexOfArray": ["$items", 2]},
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            index=INDEX_OF_ARRAY("$items", 2)
        ).get_query()
        self.assertListEqual(generated_query, query)

    def test_is_array(self):
        query = [
            {'$project':
                {'items':
                    {'$cond':
                        {
                            'if': {'$and': [{'$isArray': "$instock"}, {'$isArray': "$ordered"}]},
                            'then': {'$concatArrays': ["$instock", "$ordered"]},
                            'else': "One or more fields is not an array."
                        }
                    }
                }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            items=COND(
                _if=AND(IS_ARRAY("$instock"), IS_ARRAY("$ordered")),
                _then=CONCAT_ARRAYS("$instock", "$ordered"),
                _else="One or more fields is not an array."
            )
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_map_1(self):
        query = [
            {'$project':
                {'adjustedGrades':
                    {
                        '$map':
                            {
                                'input': "$quizzes",
                                'as': "grade",
                                'in': {'$add': ["$$grade", 2]}
                            }
                    }
                }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            adjustedGrades=MAP(
                _input="$quizzes",
                _as="grade",
                _in=ADD("$$grade", 2)
            )
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_map_2(self):
        query = [
            {'$project':
                 {'city': "$city",
                  'integerValues':
                      {'$map':
                          {
                              'input': "$distances",
                              'as': "integerValue",
                              'in': {'$trunc': "$$integerValue"}
                          }
                      }
                  }
             }
        ]

        generated_query = AggregationQueryBuilder().project(
            city="$city",
            integerValues=MAP(
                _input="$distances",
                _as="integerValue",
                _in=TRUNC("$$integerValue")
            )
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_map_3(self):
        query = [
            {'$project':
                 {'_id': 0,
                  'date': "$date",
                  'tempsStep1':
                      {'$map':
                          {
                              'input': "$temps",
                              'as': "tempInCelsius",
                              'in': {'$multiply': ["$$tempInCelsius", 9 / 5]}
                          }
                      }
                  }
             },
            {'$project':
                 {'date': "$date",
                  "temps_in_Fahrenheit":
                      {'$map':
                          {
                              'input': "$tempsStep1",
                              'as': "tempStep1",
                              'in': {'$add': ["$$tempStep1", 32]}
                          }
                      }
                  }
             }
        ]

        generated_query = AggregationQueryBuilder().project(
            id=0,
            date="$date",
            tempsStep1=MAP(_input="$temps", _as="tempInCelsius", _in=MULTIPLY("$$tempInCelsius", 9 / 5))
        ).project(
            date="$date",
            temps_in_Fahrenheit=MAP(_input="$tempsStep1", _as="tempStep1", _in=ADD("$$tempStep1", 32))
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_object_to_array(self):
        query = [
            {
                '$project': {
                    'item': 1,
                    'dimensions': {'$objectToArray': "$dimensions"}
                }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            item=1,
            dimensions=OBJECT_TO_ARRAY("$dimensions")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_object_to_array_to_sum_nested_fields(self):
        query = [
            {'$project': {'warehouses': {'$objectToArray': "$instock"}}},
            {'$unwind': "$warehouses"},
            {'$group': {'_id': "$warehouses.k", 'total': {'$sum': "$warehouses.v"}}}
        ]

        generated_query = AggregationQueryBuilder().project(
            warehouses=OBJECT_TO_ARRAY("$instock")
        ).unwind("$warehouses").group(
            id="$warehouses.k",
            total=SUM("$warehouses.v")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_object_to_array_plus_array_to_object(self):
        query = [
            {'$addFields': {'instock': {'$objectToArray': "$instock"}}},
            {'$addFields': {'instock': {'$concatArrays': ["$instock", [{"k": "total", "v": {'$sum': "$instock.v"}}]]}}},
            {'$addFields': {'instock': {'$arrayToObject': "$instock"}}}
        ]

        generated_query = AggregationQueryBuilder().add_fields(
            instock=OBJECT_TO_ARRAY("$instock")
        ).add_fields(
            instock=CONCAT_ARRAYS("$instock", [dict(k="total", v=SUM("$instock.v"))])
        ).add_fields(
            instock=ARRAY_TO_OBJECT("$instock")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_range(self):
        query = [{
            '$project': {
                '_id': 0,
                'city': 1,
                "rest_stops": {'$range': [0, "$distance", 25]}
            }}
        ]
        generated_query = AggregationQueryBuilder().project(
            id=0,
            city=1,
            rest_stops=RANGE(0, "$distance", 25)
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_reduce_multiplication(self):
        query = [{
            '$group': {
                '_id': "$experimentId",
                "probabilityArr": {'$push': "$probability"}
            }
        },
            {
                '$project': {
                    "description": 1,
                    "results": {
                        '$reduce': {
                            'input': "$probabilityArr",
                            'initialValue': 1,
                            'in': {'$multiply': ["$$value", "$$this"]}
                        }
                    }
                }
            }
        ]

        generated_query = AggregationQueryBuilder().group(
            id="$experimentId",
            probabilityArr=PUSH("$probability")
        ).project(
            description=1,
            results=REDUCE(
                _input="$probabilityArr",
                initial_value=1,
                _in=MULTIPLY("$$value", "$$this")
            )
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_reduce_discounted_merchandise(self):
        query = [
            {
                '$project': {
                    "discountedPrice": {
                        '$reduce': {
                            'input': "$discounts",
                            'initialValue': "$price",
                            'in': {'$multiply': ["$$value", {'$subtract': [1, "$$this"]}]}
                        }
                    }
                }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            discountedPrice=REDUCE(
                _input="$discounts",
                initial_value="$price",
                _in=MULTIPLY("$$value", SUBTRACT(1, "$$this"))
            )
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_reduce_string_concatenation(self):
        query = [
            {'$match': {"hobbies": {'$gt': []}}},
            {
                '$project': {
                    "name": 1,
                    "bio": {
                        '$reduce': {
                            'input': "$hobbies",
                            'initialValue': "My hobbies include:",
                            'in': {
                                '$concat': [
                                    "$$value",
                                    {
                                        '$cond': {
                                            'if': {'$eq': ["$$value", "My hobbies include:"]},
                                            'then': " ",
                                            'else': ", "
                                        }
                                    },
                                    "$$this"
                                ]
                            }
                        }
                    }
                }
            }
        ]

        generated_query = AggregationQueryBuilder().match(
            hobbies=GT()
        ).project(
            name=1,
            bio=REDUCE(
                _input="$hobbies",
                initial_value="My hobbies include:",
                _in=CONCAT(
                    "$$value",
                    COND(
                        _if=EQ("$$value", "My hobbies include:"),
                        _then=" ",
                        _else=", "
                    ),
                    "$$this"
                )
            )
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_reduce_single_reduction(self):
        query = [
            {
                '$project': {
                    "collapsed": {
                        '$reduce': {
                            'input': "$arr",
                            'initialValue': [],
                            'in': {'$concatArrays': ["$$value", "$$this"]}
                        }
                    }
                }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            collapsed=REDUCE(
                _input="$arr",
                initial_value=[],
                _in=CONCAT_ARRAYS("$$value", "$$this")
            )
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_reduce_single_reduction(self):
        query = [
            {
                '$project': {
                    "results": {
                        '$reduce': {
                            'input': "$arr",
                            'initialValue': [],
                            'in': {
                                "collapsed": {
                                    '$concatArrays': ["$$value.collapsed", "$$this"]
                                },
                                "firstValues": {
                                    '$concatArrays': ["$$value.firstValues", {'$slice': ["$$this", 1]}]
                                }
                            }
                        }
                    }
                }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            results=REDUCE(
                _input="$arr",
                initial_value=[],
                _in=dict(
                    collapsed=CONCAT_ARRAYS("$$value.collapsed", "$$this"),
                    firstValues=CONCAT_ARRAYS("$$value.firstValues", SLICE("$$this", 1))
                )
            )
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_reverse_array(self):
        query = [
            {
                '$project':
                    {
                        'name': 1,
                        'reverseFavorites': {'$reverseArray': "$favorites"}
                    }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            name=1,
            reverseFavorites=REVERSE_ARRAY("$favorites")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_size_array(self):
        query = [
            {
                '$project': {
                    'item': 1,
                    'numberOfColors': {'$size': "$colors"}
                }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            item=1,
            numberOfColors=SIZE("$colors")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_slice_array(self):
        query = [
            {'$project': {'name': 1, 'threeFavorites': {'$slice': ["$favorites", 3]}}}
        ]

        generated_query = AggregationQueryBuilder().project(
            name=1,
            threeFavorites=SLICE("$favorites", 3)
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_zip_matrix_transposition(self):
        query = [
            {
                '$project': {
                    '_id': False,
                    'transposed': {
                        '$zip': {
                            'inputs': [
                                {'$arrayElemAt': ["$matrix", 0]},
                                {'$arrayElemAt': ["$matrix", 1]},
                                {'$arrayElemAt': ["$matrix", 2]},
                            ]
                        }
                    }
                }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            id=False,
            transposed=ZIP(
                inputs=[
                    ARRAY_ELEM_AT("$matrix", 0),
                    ARRAY_ELEM_AT("$matrix", 1),
                    ARRAY_ELEM_AT("$matrix", 2)
                ]
            )
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_zip_filtering_and_preserving_indexes(self):
        query = [{
            '$project': {
                '_id': False,
                'pages': {
                    '$filter': {
                        'input': {
                            '$zip': {
                                'inputs': ["$pages", {'$range': [0, {'$size': "$pages"}]}]
                            }
                        },
                        'as': "pageWithIndex",
                        'cond': {
                            '$let': {
                                'vars': {
                                    'page': {'$arrayElemAt': ["$$pageWithIndex", 0]}
                                },
                                'in': {'$gte': ["$$page.reviews", 1]}
                            }
                        }
                    }
                }
            }
        }]

        generated_query = AggregationQueryBuilder().project(
            id=False,
            pages=FILTER(
                _input=ZIP(
                    inputs=["$pages", RANGE(0, SIZE("$pages"))],
                ),
                _as="pageWithIndex",
                cond=LET(
                    expr=dict(page=ARRAY_ELEM_AT("$$pageWithIndex", 0)),
                    _in=GTE("$$page.reviews", 1)
                )
            )
        ).get_query()

        self.assertListEqual(generated_query, query)


if __name__ == '__main__':
    unittest.main()
