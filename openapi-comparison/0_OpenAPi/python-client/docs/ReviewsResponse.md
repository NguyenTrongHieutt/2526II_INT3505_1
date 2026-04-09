# ReviewsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Review]**](Review.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.reviews_response import ReviewsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewsResponse from a JSON string
reviews_response_instance = ReviewsResponse.from_json(json)
# print the JSON string representation of the object
print(ReviewsResponse.to_json())

# convert the object into a dict
reviews_response_dict = reviews_response_instance.to_dict()
# create an instance of ReviewsResponse from a dict
reviews_response_from_dict = ReviewsResponse.from_dict(reviews_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


