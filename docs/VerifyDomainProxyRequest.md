# VerifyDomainProxyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | The ID of the domain that will be updated. | [optional] 
**proxy_url** | **str** | The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. e.g. https://example.com/__clerk | [optional] 

## Example

```python
from clerk_backend_sdk.models.verify_domain_proxy_request import VerifyDomainProxyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyDomainProxyRequest from a JSON string
verify_domain_proxy_request_instance = VerifyDomainProxyRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyDomainProxyRequest.to_json())

# convert the object into a dict
verify_domain_proxy_request_dict = verify_domain_proxy_request_instance.to_dict()
# create an instance of VerifyDomainProxyRequest from a dict
verify_domain_proxy_request_from_dict = VerifyDomainProxyRequest.from_dict(verify_domain_proxy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


