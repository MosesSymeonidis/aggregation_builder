from Utils.AggregationBuilder.AggregationBuilder import AggregationQueryBuilder
from Utils.AggregationBuilder.Operators import *
import unittest


class GroupOperatorsTests(unittest.TestCase):
    def test_sum_at_group_stage(self):
        query = [
            {
                '$group':
                    {
                        '_id': {'day': {'$dayOfYear': "$date"}, 'year': {'$year': "$date"}},
                        'totalAmount': {'$sum': {'$multiply': ["$price", "$quantity"]}},
                        'count': {'$sum': 1}
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().group(id=dict(
            day=DAY_OF_YEAR("$date"),
            year=YEAR("$date")
        ), totalAmount=SUM(MULTIPLY("$price", "$quantity")), count=SUM(1)).get_query()

        self.assertListEqual(generated_query, query)

    def test_sum_at_project_stage(self):
        query = [
            {
                '$project':
                    {
                        'quizTotal': {'$sum': "$quizzes"},
                        'labTotal': {'$sum': '$labs'},
                        'examTotal': {'$sum': ["$final", "$midterm"]}
                    }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            quizTotal=SUM('$quizzes'),
            labTotal=SUM('$labs'),
            examTotal=SUM("$final", "$midterm")
        ).get_query()
        self.assertListEqual(generated_query, query)

    def test_avg_at_group_stage(self):
        query = [
            {
                '$group':
                    {
                        '_id': "$item",
                        'avgAmount': {'$avg': {'$multiply': ["$price", "$quantity"]}},
                        'avgQuantity': {'$avg': "$quantity"}
                    }
            }
        ]

        generated_query = AggregationQueryBuilder().group(
            id="$item",
            avgAmount=AVG(MULTIPLY("$price", "$quantity")),
            avgQuantity=AVG("$quantity")
        ).get_query()
        self.assertListEqual(generated_query, query)

    def test_avg_at_project_stage(self):
        query = [
            {
                '$project': {
                    'quizAvg': {'$avg': "$quizzes"},
                    'labAvg': {'$avg': "$labs"},
                    'examAvg': {'$avg': ["$final", "$midterm"]}
                }
            }
        ]

        generated_query = AggregationQueryBuilder().project(
            quizAvg=AVG("$quizzes"),
            labAvg=AVG("$labs"),
            examAvg=AVG("$final", "$midterm")
        ).get_query()
        self.assertListEqual(generated_query, query)

    def test_first(self):
        query = [
            {'$sort': {'item': 1, 'date': 1}},
            {
                '$group':
                    {
                        '_id': "$item",
                        'firstSalesDate': {'$first': "$date"}
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().sort(
            item=1,
            date=1).group(
            id='item',
            firstSalesDate=FIRST("$date")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_last(self):
        query = [
            {'$sort': {'item': 1, 'date': 1}},
            {
                '$group':
                    {
                        '_id': "$item",
                        'lastSalesDate': {'$last': "$date"}
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().sort(
            item=1,
            date=1).group(
            id='item',
            lastSalesDate=LAST("$date")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_max_at_group_stage(self):
        query = [
            {
                '$group':
                    {
                        '_id': "$item",
                        'maxTotalAmount': {'$max': {'$multiply': ["$price", "$quantity"]}},
                        'maxQuantity': {'$max': "$quantity"}
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().group(
            id='item',
            maxTotalAmount=MAX(MULTIPLY("$price", "$quantity")),
            maxQuantity=MAX("$quantity")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_max_at_project_stage(self):
        query = [
            {
                '$project': {
                    'quizMax': {'$max': "$quizzes"},
                    'labMax': {'$max': "$labs"},
                    'examMax': {'$max': ["$final", "$midterm"]}
                }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            quizMax=MAX('$quizzes'),
            labMax=MAX("$labs"),
            examMax=MAX("$final", "$midterm")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_min_at_group_stage(self):
        query = [
            {
                '$group':
                    {
                        '_id': "$item",
                        'minQuantity': {'$min': "$quantity"}
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().group(
            id='item',
            minQuantity=MIN("$quantity")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_min_at_project_stage(self):
        query = [
            {
                '$project': {
                    'quizMin': {'$min': "$quizzes"},
                    'labMin': {'$min': "$labs"},
                    'examMin': {'$min': ["$final", "$midterm"]}
                }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            quizMin=MIN('$quizzes'),
            labMin=MIN("$labs"),
            examMin=MIN("$final", "$midterm")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_push(self):
        query = [
            {
                '$group': {
                    '_id': {'day': {'$dayOfYear': "$date"}, 'year': {'$year': "$date"}},
                    'itemsSold': {'$push': {'item': "$item", 'quantity': "$quantity"}}
                }
            }
        ]
        generated_query = AggregationQueryBuilder().group(
            id=dict(day=DAY_OF_YEAR("$date"), year=YEAR("$date")),
            itemsSold=PUSH(dict(item="$item", quantity="$quantity"))
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_add_to_set(self):
        query = [
            {
                '$group': {
                    '_id': {'day': {'$dayOfYear': "$date"}, 'year': {'$year': "$date"}},
                    'itemsSold': {'$addToSet': "$item"}
                }
            }
        ]
        generated_query = AggregationQueryBuilder().group(
            id=dict(day=DAY_OF_YEAR("$date"), year=YEAR("$date")),
            itemsSold=ADD_TO_SET("$item")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_stdDev_at_group_stage(self):
        query = [
            {
                '$group':
                    {
                        '_id': "$quiz",
                        'stdDev': {'$stdDevPop': "$score"}
                    }
            }
        ]
        generated_query = AggregationQueryBuilder().group(
            id='quiz',
            stdDev=STD_DEV_POP("$score")
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_stdDev_at_project_stage(self):
        query = [
            {
                '$project': {
                    'stdDev': {'$stdDevPop': "$scores.score"}
                }
            }
        ]
        generated_query = AggregationQueryBuilder().project(
            stdDev=STD_DEV_POP('$scores.score')
        ).get_query()

        self.assertListEqual(generated_query, query)

    def test_stdDevSamp(self):
        query = [
            {'$sample': {'size': 100}},
            {'$group': {'_id': None, 'ageStdDev': {'$stdDevSamp': "$age"}}}
        ]
        generated_query = AggregationQueryBuilder().sample(100).group(
            id=None,
            ageStdDev=STD_DEV_SAMP('$age')
        ).get_query()
        self.assertListEqual(generated_query, query)


if __name__ == '__main__':
    unittest.main()
