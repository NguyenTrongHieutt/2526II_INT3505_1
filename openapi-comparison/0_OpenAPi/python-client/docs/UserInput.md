# UserInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from openapi_client.models.user_input import UserInput

# TODO update the JSON string below
json = "{}"
# create an instance of UserInput from a JSON string
user_input_instance = UserInput.from_json(json)
# print the JSON string representation of the object
print(UserInput.to_json())

# convert the object into a dict
user_input_dict = user_input_instance.to_dict()
# create an instance of UserInput from a dict
user_input_from_dict = UserInput.from_dict(user_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


