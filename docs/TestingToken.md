# TestingToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**token** | **str** | The actual token. This value is meant to be passed in the &#x60;__clerk_testing_token&#x60; query parameter with requests to the Frontend API. | 
**expires_at** | **int** | Unix timestamp of the token&#39;s expiration time.  | 

## Example

```python
from clerk_backend_sdk.models.testing_token import TestingToken

# TODO update the JSON string below
json = "{}"
# create an instance of TestingToken from a JSON string
testing_token_instance = TestingToken.from_json(json)
# print the JSON string representation of the object
print(TestingToken.to_json())

# convert the object into a dict
testing_token_dict = testing_token_instance.to_dict()
# create an instance of TestingToken from a dict
testing_token_from_dict = TestingToken.from_dict(testing_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


