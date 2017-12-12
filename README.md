# aggregation_builder

This is a library that generates programmatically aggregation queries for mongodb. 


## Getting Started

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

### Installing

You can install library via setup file simple by:


```
python setup.py install
```

or via pip, in project folder you can run:

```
pip install .
```

Finally, you can just copy the aggregation_builder folder in your project and import the modules that you want.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* The main purpose of this library is to handle mongo's aggregation framework. For this reason, hall library is based on [aggregation framework faculties](https://docs.mongodb.com/v3.4/aggregation/)

* This library is inspired by [MongoEngine](http://mongoengine.org/) thus is created as an extra tool of this
