# CreateRedirectURLRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The full url value prefixed with &#x60;https://&#x60; or a custom scheme e.g. &#x60;\&quot;https://my-app.com/oauth-callback\&quot;&#x60; or &#x60;\&quot;my-app://oauth-callback\&quot;&#x60; | [optional] 

## Example

```python
from clerk_backend_sdk.models.create_redirect_url_request import CreateRedirectURLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRedirectURLRequest from a JSON string
create_redirect_url_request_instance = CreateRedirectURLRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRedirectURLRequest.to_json())

# convert the object into a dict
create_redirect_url_request_dict = create_redirect_url_request_instance.to_dict()
# create an instance of CreateRedirectURLRequest from a dict
create_redirect_url_request_from_dict = CreateRedirectURLRequest.from_dict(create_redirect_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


