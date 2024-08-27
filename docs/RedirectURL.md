# RedirectURL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**url** | **str** |  | 
**created_at** | **int** | Unix timestamp of creation.  | 
**updated_at** | **int** | Unix timestamp of last update.  | 

## Example

```python
from clerk_backend_sdk.models.redirect_url import RedirectURL

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectURL from a JSON string
redirect_url_instance = RedirectURL.from_json(json)
# print the JSON string representation of the object
print(RedirectURL.to_json())

# convert the object into a dict
redirect_url_dict = redirect_url_instance.to_dict()
# create an instance of RedirectURL from a dict
redirect_url_from_dict = RedirectURL.from_dict(redirect_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


