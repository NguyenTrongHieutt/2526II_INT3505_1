# BookInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**author** | **str** |  | 

## Example

```python
from openapi_client.models.book_input import BookInput

# TODO update the JSON string below
json = "{}"
# create an instance of BookInput from a JSON string
book_input_instance = BookInput.from_json(json)
# print the JSON string representation of the object
print(BookInput.to_json())

# convert the object into a dict
book_input_dict = book_input_instance.to_dict()
# create an instance of BookInput from a dict
book_input_from_dict = BookInput.from_dict(book_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


