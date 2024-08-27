# VerifyClientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | A JWT that represents the active client. | [optional] 

## Example

```python
from clerk_backend_sdk.models.verify_client_request import VerifyClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyClientRequest from a JSON string
verify_client_request_instance = VerifyClientRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyClientRequest.to_json())

# convert the object into a dict
verify_client_request_dict = verify_client_request_instance.to_dict()
# create an instance of VerifyClientRequest from a dict
verify_client_request_from_dict = VerifyClientRequest.from_dict(verify_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


