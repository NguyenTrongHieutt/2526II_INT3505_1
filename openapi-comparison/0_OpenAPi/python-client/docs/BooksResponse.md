# BooksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Book]**](Book.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.books_response import BooksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BooksResponse from a JSON string
books_response_instance = BooksResponse.from_json(json)
# print the JSON string representation of the object
print(BooksResponse.to_json())

# convert the object into a dict
books_response_dict = books_response_instance.to_dict()
# create an instance of BooksResponse from a dict
books_response_from_dict = BooksResponse.from_dict(books_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


