from mongoengine.queryset import QuerySet
from aggregation_builder import AggregationQueryBuilder


class AggregateQuerySet(QuerySet):
    __AggregationQueryBuilder__ = AggregationQueryBuilder

    @property
    def aggregation_builder(self):
        return self.__AggregationQueryBuilder__(self)
