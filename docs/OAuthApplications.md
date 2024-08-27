# OAuthApplications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OAuthApplication]**](OAuthApplication.md) |  | 
**total_count** | **int** | Total number of OAuth applications  | 

## Example

```python
from clerk_backend_sdk.models.o_auth_applications import OAuthApplications

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthApplications from a JSON string
o_auth_applications_instance = OAuthApplications.from_json(json)
# print the JSON string representation of the object
print(OAuthApplications.to_json())

# convert the object into a dict
o_auth_applications_dict = o_auth_applications_instance.to_dict()
# create an instance of OAuthApplications from a dict
o_auth_applications_from_dict = OAuthApplications.from_dict(o_auth_applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


