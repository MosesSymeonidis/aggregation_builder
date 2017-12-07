#aggregation_builder

This is a library that generates programmatically aggregation queries for mongodb. 

For example the following aggregation query:
```
db.collection.aggregate(
    [
        {
            '$group':
                {
                    '_id': "$item",
                    'avgAmount': {'$avg': {'$multiply': ["$price", "$quantity"]}},
                    'avgQuantity': {'$avg': "$quantity"}
                }
        }
    ]
)
```

will be executed by libarary like:

```python

aggregation_builder(collection).group(
    id="$item",
    avgAmount=AVG(MULTIPLY("$price", "$quantity")),
    avgQuantity=AVG("$quantity")
).aggregate()

```

Moreover, if you decide to use MongoEngine library you can use AggregateQuerySet class that provides you the ability to execute aggregations via mongoengine model. For instance:

```python
class Traffic(DynamicDocument):
    meta = {'queryset_class': AggregateQuerySet}
    
Traffic.objects.aggregation_builder.group(id='response.data',first_obj=FIRST('$$ROOT')).skip(5).limit(7).execute()
```