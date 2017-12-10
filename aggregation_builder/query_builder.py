import pymongo

__version__ = '0.0.1'

if pymongo.version_tuple[0] < 3:
    IS_PYMONGO_3 = False
else:
    IS_PYMONGO_3 = True


class AggregationQueryBuilder(object):

    def __init__(self, query_set_obj=None, raw=None):
        self._q = []
        if raw:
            self.add_raw(raw=raw)
        self.query_set_obj = query_set_obj

    def get_query(self):
        """
        Getter function for the query
        :return: The dictionary of the query
        """
        return self._q

    def add_raw(self, raw):
        """
        Adds row aggregation state at the query
        :param raw: list of raw stages or a dict of raw stage
        :return: The current object
        """
        if type(raw) == list:
            self._q += raw
        if type(raw) == dict:
            self._q.append(raw)
        return self

    def limit(self, limit):
        """
        Adds limit stage at the query
        :param limit: The number of documents
        :return: The current object
        """
        self._q.append({'$limit': limit})
        return self

    def skip(self, skip):
        """
        Adds skip stage at the query
        :param skip: The number of documents
        :return: The current object
        """
        self._q.append({'$skip': skip})
        return self

    def project(self, id=None, *args, **kwargs):
        """
        Adds a projection stage at the query
        :param id: Specifies if the id is in selected fields default value is None
        :param args: The list of the fields that will be project
        :param kwargs: The fields that will be generated
        :return:
        """
        projection = {}

        if id is not None:
            projection['_id'] = id

        for arg in args:
            projection[arg] = 1

        for kwarg in kwargs:
            projection[kwarg] = kwargs[kwarg]

        self._q.append({
            '$project': projection
        })

        return self

    def match(self, **query):
        """
        Adds a match stage at the query
        :param query: The parameters of the query
        :return: The current object
        """
        self._q.append({'$match': query})
        return self

    def group(self, id=None, **kwargs):
        """
        Adds a group stage at aggregation query
        :param id: The group id. Default value is None and group merge all documents
        :param kwargs: The parameters-methods of group stage
        :return: The current object
        """
        if type(id) == str:
            if not id.startswith('$'):
                id = '$' + id
        query = {
            '_id': id
        }
        for key in kwargs:
            query[key] = kwargs[key]
        self._q.append({
            '$group': query
        })
        return self

    def unwind(self, path, include_array_index=None, preserve_null_and_empty_arrays=False):
        """
        Adds an unwind stage to deconstruct an array
        :param path: Field path to an array field
        :param include_array_index: The name of a new field to hold the array index of the element.
        :param preserve_null_and_empty_arrays:
            If true, if the path is null, missing, or an empty array, $unwind outputs the document.
            If false, $unwind does not output a document if the path is null, missing, or an empty array.
        :return: The current object
        """
        unwind_query = {}
        unwind_query['$unwind'] = path if path[0] == '$' else '$' + path

        if include_array_index:
            unwind_query['includeArrayIndex'] = include_array_index
        if preserve_null_and_empty_arrays:
            unwind_query['preserveNullAndEmptyArrays'] = True
        self._q.append(unwind_query)
        return self

    def sort(self, **kwargs):
        """
        Adds a sort stage to aggregation query
        :param kwargs: Specifies the field(s) to sort by and the respective sort order.
        :return: The current object
        """
        query = {}
        for field in kwargs:
            if kwargs[field] in [1, -1]:
                query[field] = kwargs[field]
        self._q.append({'$sort': query})
        return self

    def sample(self, size=100):
        """
        Randomly selects the specified number of documents from its input.
        :param size: The size of sample
        :return: The current object
        """
        self._q.append({'$sample': {'size': size}})
        return self

    def look_up(self, _from, _localField, _foreignField, _as):
        """
        Adds look up stage at query (left outer join)
        :param _from: Specifies the collection in the same database to perform the join with.
        :param _localField: Specifies the field from the documents input to the $lookup stage.
        :param _foreignField: Specifies the field from the documents in the from collection.
        :param _as: Specifies the name of the new array field to add to the input documents.
        :return: The current object
        """
        query = {
            'from': _from,
            'localField': _localField,
            'foreignField': _foreignField,
            'as': _as
        }
        self._q.append({'$lookup': query})
        return self

    def graph_look_up(self, _from, _startWith, _connectFromField, _connectToField,
                      _as, _maxDepth=None, _depthField=None, _restrictSearchWithMatch=None):
        """
        Performs a recursive search on a collection, with options for restricting the search by recursion depth and query filter.
        :param _from: Target collection for the $graphLookup operation to search, recursively matching the connectFromField to the connectToField.
        :param _startWith: Expression that specifies the value of the connectFromField with which to start the recursive search.
        :param _connectFromField: Field name whose value $graphLookup uses to recursively match against the connectToField of other documents in the collection.
        :param _connectToField: Field name in other documents against which to match the value of the field specified by the connectFromField parameter.
        :param _as: Name of the array field added to each output document.
        :param _maxDepth: Non-negative integral number specifying the maximum recursion depth.
        :param _depthField: Name of the field to add to each traversed document in the search path.
        :param _restrictSearchWithMatch: A document specifying additional conditions for the recursive search.
        :return: The current object
        """
        query = {
            'from': _from,
            'startWith': _startWith,
            'connectFromField': _connectFromField,
            'connectToField': _connectToField,
            'as': _as
        }
        if _maxDepth:
            query['maxDepth'] = _maxDepth
        if _depthField:
            query['depthField'] = _depthField
        if _restrictSearchWithMatch:
            query['restrictSearchWithMatch'] = _restrictSearchWithMatch
        self._q.append({'$graphLookup': query})
        return self

    def add_fields(self, **fields):
        """
        Adds a stage to aggregation query which adds new fields to documents.
        :param fields: The fields that will be created
        :return: The current object
        """
        query = {}
        for field in fields:
            query[field] = fields[field]
        self._q.append({'$addFields': query})
        return self

    def __str__(self):
        return str(self._q)

    def execute(self):
        """
        Executes the query if self.query_set_obj is set
        :return: The result of aggregation query
        """
        if self.query_set_obj is None:
            return []
        result = self.query_set_obj.aggregate(*self.get_query())
        if IS_PYMONGO_3:
            result = list(result)
        else:
            result = result.get('result')
        if result:
            return result
        return []

    def aggregate(self):
        """
        Executes the query if self.query_set_obj is set
        :return: The result of aggregation query
        """
        return self.execute()
