# VerifySessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The JWT that is sent via the &#x60;__session&#x60; cookie from your frontend. Note: this JWT must be associated with the supplied session ID. | [optional] 

## Example

```python
from clerk_backend_sdk.models.verify_session_request import VerifySessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifySessionRequest from a JSON string
verify_session_request_instance = VerifySessionRequest.from_json(json)
# print the JSON string representation of the object
print(VerifySessionRequest.to_json())

# convert the object into a dict
verify_session_request_dict = verify_session_request_instance.to_dict()
# create an instance of VerifySessionRequest from a dict
verify_session_request_from_dict = VerifySessionRequest.from_dict(verify_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


